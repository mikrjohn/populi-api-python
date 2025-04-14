import logging
import pycurl
import json
from io import BytesIO
import time
from urllib.parse import urlencode
from os import environ

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
    
    # Set headers for JSON content
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json', 'Content-Type: application/x-www-form-urlencoded'])

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

        (response, json_data) = driver.call_populi(parameters, skip_access_key=True)

        return json_data.get('access_key')

    @staticmethod
    def call_populi(parameters, skip_access_key=False, raw_data=False):
        retry = 1
        while True:
            try:
                if skip_access_key is False:
                    parameters.update({'access_key': driver.access_key})

                for p in list(parameters.keys()):
                    if isinstance(parameters[p], list) and p[-2:] != '[]':
                        parameters[p+'[]'] = parameters[p]
                        del parameters[p]

                b = request(driver.endpoint, parameters, curl_options=driver.curl_options)

                if raw_data:
                    return b, None

                try:
                    json_data = json.loads(b.getvalue().decode('utf-8'))
                    
                    # Check for errors
                    if 'error' in json_data:
                        driver.raise_exception(json_data['error'])
                    
                    return b, json_data
                except json.JSONDecodeError as e:
                    # Handle case where response is not valid JSON
                    logger.error(f"JSON parse error: {e}")
                    logger.debug(f"Response content: {b.getvalue().decode('utf-8')}")
                    raise exceptions.OtherError(f"Invalid JSON response: {e}")
                    
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
    def raise_exception(error):
        msg = error.get('message', 'Unknown error')
        code = error.get('code', 'OTHER_ERROR')

        try:
            raise exceptions.exception_lookup[code](msg)
        except KeyError:
            raise exceptions.exception_lookup['OTHER_ERROR'](msg)

    @staticmethod
    def get_all_anonymous(task='', root_element='', **kwargs):
        """
        Handle paginated results with the JSON API
        
        For JSON API, we'll collect all pages into a single result array
        """
        logger.debug(f"Executing {task}")

        kwargs['page'] = 1
        kwargs['task'] = task
        total_results = 1
        current_count = 0
        all_results = []
        metadata = {}

        while current_count < total_results:
            logger.debug(f"Page {kwargs['page']}")

            (result, json_data) = driver.call_populi(kwargs)
            
            # Extract the results based on the root_element if present
            results = json_data.get(root_element, [])
            if not results and isinstance(json_data, dict):
                # If no root element is found, look for any array in the response
                for key, value in json_data.items():
                    if isinstance(value, list):
                        results = value
                        if not root_element:
                            root_element = key
                        break
            
            # Extract metadata
            if isinstance(json_data, dict):
                metadata = {k: v for k, v in json_data.items() if not isinstance(v, list)}
                
                # Check for total number of results if available
                if 'total' in metadata:
                    total_results = metadata['total']
                elif 'num_results' in metadata:
                    total_results = metadata['num_results']
                else:
                    # If total count not available, assume we're done after this page
                    total_results = current_count + len(results)
            
            # Add the results to our collection
            all_results.extend(results)
            current_count += len(results)
            
            logger.debug(f"Page: {kwargs['page']} ({current_count}/{total_results})")
            
            kwargs['page'] += 1
            
            # Check if there are more pages
            if len(results) == 0 or current_count >= total_results:
                break

        # Create a complete response with all results
        complete_response = metadata.copy()
        complete_response[root_element] = all_results
        
        return json.dumps(complete_response), complete_response


use_native = False


def initialize(
        endpoint: str="",
        username: str="",
        password: str="",
        access_key: str=None,
        asXML: bool=False,  # Kept for backward compatibility, renamed to use_native
        curl_options: (list, tuple)=[]):
    global use_native
    # asXML is now a flag for using native JSON objects vs string
    use_native = asXML

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

    logger.debug(f"Executing {task}")

    (result, json_data) = driver.call_populi(new_kwargs, raw_data=raw_data)

    if json_data is None:
        return result.read()

    if use_native:
        return json_data
    else:
        return json.dumps(json_data)


def get_all_anonymous(task, root_element='', **kwargs):
    new_kwargs = {}

    for argc, argv in kwargs.items():
        if argv is not None:
            new_kwargs[argc] = argv

    (result, json_data) = driver.get_all_anonymous(
        task=task, root_element=root_element, **new_kwargs)

    if use_native:
        return json_data
    else:
        return result
