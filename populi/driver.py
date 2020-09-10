import logging
import pycurl
import lxml.etree as etree
from io import BytesIO
import time
from urllib.parse import urlencode
from os import environ, path

from . import exceptions

logger = logging.getLogger(__name__)
request_count = 0


def request(endpoint, parameters, curl_options=[]):
    global request_count

    request_count += 1

    c = pycurl.Curl()
    b = BytesIO()

    c.setopt(pycurl.URL, endpoint)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, urlencode(parameters, True))
    c.setopt(pycurl.WRITEDATA, b)

    for opt_name, opt_value in curl_options:
        c.setopt(opt_name, opt_value)

    c.perform()

    response_code = c.getinfo(pycurl.RESPONSE_CODE)

    c.close()

    if response_code == 429:
        raise exceptions.TooManyRequests('Too many requests')

    b.seek(0)

    return b


class TooManyRequests(exceptions.TooManyRequests):
    pass


class driver(object):
    endpoint = None
    access_key = None
    curl_options = None

    @staticmethod
    def initialize(endpoint: str = "", username: str = "", password: str = "", access_key: str = None, curl_options: list = []):

        driver.endpoint = environ['populiEndpoint'] if endpoint == "" else endpoint
        driver.endpoint = driver.endpoint.strip('\n').replace('\"', '')
        driver.curl_options = curl_options

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

        (response, xml) = driver.call_populi(parameters, skip_access_key=True)

        return xml.find('access_key').text

    @staticmethod
    def call_populi(parameters, skip_access_key=False, raw_data=False):
        retry = 1
        while True:
            try:
                if skip_access_key is False:
                    parameters.update({'access_key': driver.access_key})

                for p in parameters.keys():
                    if isinstance(parameters[p], list) and p[-2:] != '[]':
                        parameters[p+'[]'] = parameters[p]
                        del parameters[p]

                b = request(driver.endpoint, parameters, curl_options=driver.curl_options)

                if raw_data:
                    return b, None

                xml = etree.parse(b).getroot()

                if xml.xpath('/error'):
                    driver.raise_exception(xml)

                return b, xml
            except exceptions.TooManyRequests:
                time.sleep(retry)
                retry += retry
            except exceptions.BasePopuliException:
                raise
            except BaseException as e:
                print("Other Error: {}".format(e), end="", flush=True)
                print(repr(driver.endpoint), flush=True)
                print(repr(urlencode(parameters)), flush=True)
                raise

    @staticmethod
    def raise_exception(xml):
        msg = xml.xpath('/error/message/text()')[0]
        code = xml.xpath('/error/code/text()')[0]

        try:
            raise exceptions.exception_lookup[code](msg)
        except KeyError:
            raise exceptions.exception_lookup['OTHER_ERROR'](msg)

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

            (result, xml) = driver.call_populi(kwargs)
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

        xml_string = etree.tostring(master, xml_declaration=True, encoding="UTF-8")

        return xml_string, master


use_lxml = False


def initialize(
        endpoint: str="",
        username: str="",
        password: str="",
        access_key: str=None,
        asXML: bool=False,
        curl_options: (list, tuple)=[]):
    global use_lxml
    use_lxml = asXML

    driver.initialize(
        endpoint=endpoint,
        username=username,
        password=password,
        access_key=access_key,
        curl_options=curl_options)


def get_anonymous(task, raw_data=False, **kwargs):
    new_kwargs = {}

    for argc, argv in kwargs.items():
        if argv is not None:
            new_kwargs[argc] = argv

    new_kwargs.update({'task': task})

    logger.debug("Executing %s" % task)

    (result, xml) = driver.call_populi(new_kwargs, raw_data=raw_data)

    if xml is None:
        return result.read()

    if use_lxml:
        if xml.tag == 'code':
            raise exceptions.OtherError(xml.text)
        return xml
    else:
        return result.getvalue().decode('UTF-8')


def get_all_anonymous(task, root_element, **kwargs):
    new_kwargs = {}

    for argc, argv in kwargs.items():
        if argv is not None:
            new_kwargs[argc] = argv

    (result, xml) = driver.get_all_anonymous(
        task=task, root_element=root_element, **new_kwargs)

    if use_lxml:
        if xml.tag == 'code':
            raise exceptions.OtherError(xml.text)
        return xml
    else:
        return result.decode('UTF-8')
