import logging
import pycurl
import lxml.etree as etree
from io import BytesIO
import time
from urllib.parse import urlencode
from os import environ


logger = logging.getLogger(__name__)
request_count = 0


def request(endpoint, parameters):
    global request_count

    request_count += 1

    c = pycurl.Curl()
    b = BytesIO()

    c.setopt(pycurl.URL, endpoint)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, urlencode(parameters, True))
    c.setopt(pycurl.WRITEDATA, b)
    c.perform()
    c.close()
    b.seek(0)

    return b


class TooManyRequests(Exception):
    pass


class driver(object):
    endpoint = None
    access_key = None

    @staticmethod
    def initialize(endpoint: str = "", username: str = "", password: str = "", access_key: str = None):

        driver.endpoint = environ['populiEndpoint'] if endpoint == "" else endpoint
        driver.endpoint = driver.endpoint.strip('\n').replace('\"', '')

        logger.info("Initializing Populi Driver")

        if access_key is None:
            username = environ['populiUser'] if username == "" else username
            password = environ['populiPassword'] if password == "" else password

            driver.access_key = driver.generate_access_key(username=username, password=password)
        else:
            driver.access_key = access_key

    @staticmethod
    def generate_access_key(username="", password=""):
        logger.debug("Generating Access Key")

        parameters = {
            'username': username,
            'password': password
        }

        response = driver.call_populi(parameters, skip_access_key=True)

        xml = etree.parse(response)
        return xml.find('access_key').text

    @staticmethod
    def call_populi(parameters, skip_access_key=False):
        retry = 1
        while True:
            try:
                if skip_access_key is False:
                    parameters.update({'access_key': driver.access_key})

                for p in parameters.keys():
                    if isinstance(parameters[p], list) and p[-2:] != '[]':
                        parameters[p+'[]'] = parameters[p]
                        del parameters[p]

                b = request(driver.endpoint, parameters)

                xml = etree.parse(b).getroot()
                if xml.xpath('//error/code[text()="429"]'):
                    raise TooManyRequests('Too Many Requests')
                return b
            except TooManyRequests:
                time.sleep(retry)
                retry += retry
            except BaseException as e:
                print("Other Error: {}".format(e), end="", flush=True)
                print(repr(driver.endpoint), flush=True)
                print(repr(urlencode(parameters)), flush=True)
                logger.warning('Retrying Curl Execution')
                time.sleep(retry)
                retry += retry

    @staticmethod
    def get_anonymous(task='', **kwargs):
        kwargs.update({'task': task})

        logger.debug("Executing %s" % task)

        api_response = driver.call_populi(kwargs)

        return api_response.getvalue().decode('UTF-8')

    @staticmethod
    def get_all_anonymous(task='', root_element='', **kwargs):

        logger.debug("Executing %s" % task)

        kwargs['page'] = 1
        kwargs['task'] = task
        total = 1
        curr = 0
        master = None
        subelement = False

        while total > curr:
            logger.debug("Page %d" % kwargs['page'])

            result = driver.call_populi(kwargs)
            xml = etree.parse(result).getroot()
            total = int(xml.get('num_results'))

            els = xml.findall(root_element)
            if not els and len(xml.getchildren()) == 1:
                els = xml[0].findall(root_element)
                subelement = True

            curr += len(els)

            if master is None:
                master = xml
            else:
                for elt in els:
                    if subelement:
                        master.getchildren()[0].append(elt)
                    else:
                        master.append(elt)
            logger.debug("Page: %d (%d/%d)" % (kwargs['page'], curr, total))

            kwargs['page'] += 1

        xml_string = etree.tostring(master, xml_declaration=True, encoding="ISO-8859-1")

        return xml_string


use_lxml = False


def initialize(
        endpoint="",
        username="",
        password="",
        access_key=None,
        asXML=False):
    global use_lxml
    use_lxml = asXML

    driver.initialize(
        endpoint=endpoint,
        username=username,
        password=password,
        access_key=access_key)


def get_anonymous(task, **kwargs):
    new_kwargs = {}

    for argc, argv in kwargs.items():
        if argv is not None:
            new_kwargs[argc] = argv

    result = driver.get_anonymous(task=task, **new_kwargs)

    if use_lxml:
        xml = etree.fromstring(result.encode('UTF-8'))
        if xml.tag == 'code':
            raise Exception(xml.text)
        return xml
    else:
        return result


def get_all_anonymous(task, root_element, **kwargs):
    new_kwargs = {}

    for argc, argv in kwargs.items():
        if argv is not None:
            new_kwargs[argc] = argv

    result = driver.get_all_anonymous(
        task=task, root_element=root_element, **new_kwargs)

    if use_lxml:
        xml = etree.fromstring(result)
        if xml.tag == 'code':
            raise Exception(xml.text)
        return xml
    else:
        return result.decode('UTF-8')
