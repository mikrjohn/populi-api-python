from nose.tools import *
import unittest
from unittest.mock import call, patch, MagicMock
from io import BytesIO
from urllib.parse import urlencode
import lxml.etree as etree
import os.path

from populi import driver
from populi import exceptions


class TestDriver(unittest.TestCase):

    @patch('populi.driver.BytesIO')
    @patch('populi.driver.pycurl')
    def test_request_with_additional_curl_options(self, mock_pycurl, mock_BytesIO):
        bio = BytesIO()
        expected_html = b'<html><body><p>Test</p></body></html>'
        bio.write(expected_html)
        mock_BytesIO.return_value = bio
        driver.request_count = 0

        mock_pycurl.URL = 'URL'
        mock_pycurl.POST = 'POST'
        mock_pycurl.POSTFIELDS = 'POSTFIELDS'
        mock_pycurl.WRITEDATA = 'WRITEDATA'
        mock_curl = MagicMock()
        mock_pycurl.Curl.return_value = mock_curl

        result = driver.request('endpoint', {'p': 'v'}, (('a', 1), ('b', 2), ('c', 4)))

        mock_curl.setopt.assert_has_calls(
            [
                call(mock_pycurl.URL, 'endpoint'),
                call(mock_pycurl.POST, 1),
                call(mock_pycurl.POSTFIELDS, urlencode({'p': 'v'}, True)),
                call(mock_pycurl.WRITEDATA, bio),
                call('a', 1),
                call('b', 2),
                call('c', 4)
            ],
            any_order=True
        )

    @patch('populi.driver.BytesIO')
    @patch('populi.driver.pycurl')
    def test_request(self, mock_pycurl, mock_BytesIO):
        bio = BytesIO()
        expected_html = b'<html><body><p>Test</p></body></html>'
        bio.write(expected_html)
        mock_BytesIO.return_value = bio
        driver.request_count = 0

        mock_pycurl.URL = 'URL'
        mock_pycurl.POST = 'POST'
        mock_pycurl.POSTFIELDS = 'POSTFIELDS'
        mock_pycurl.WRITEDATA = 'WRITEDATA'
        mock_curl = MagicMock()
        mock_pycurl.Curl.return_value = mock_curl

        result = driver.request('endpoint', {'p': 'v'})

        mock_curl.setopt.assert_has_calls(
            [
                call(mock_pycurl.URL, 'endpoint'),
                call(mock_pycurl.POST, 1),
                call(mock_pycurl.POSTFIELDS, urlencode({'p': 'v'}, True)),
                call(mock_pycurl.WRITEDATA, bio)
            ],
            any_order = True
        )
        mock_curl.perform.assert_called_once_with()
        mock_curl.close.assert_called_once_with()

        self.assertEqual(result, bio)
        self.assertEqual(result.getvalue(), expected_html)
        self.assertEqual(1, driver.request_count)

        driver.request('endpoint', {'v': 'p'})

        self.assertEqual(2, driver.request_count)

    @patch('populi.driver.driver.initialize')
    def test_initialize_connects_to_initialize(self, mock_initialize):
        endpoint='ENDPOINT'
        username='USERNAME'
        password='PASSWORD',
        access_key='ACCESS_KEY',
        asXML='AS XML'
        curl_options='CURL_OPTIONS'

        driver.use_lxml = False

        driver.initialize(
            endpoint=endpoint,
            username=username,
            password=password,
            access_key=access_key,
            asXML=asXML,
            curl_options=curl_options
        )

        mock_initialize.assert_called_once_with(
            endpoint=endpoint,
            username=username,
            password=password,
            access_key=access_key,
            curl_options=curl_options
        )

        self.assertEqual(driver.use_lxml, asXML)

    @patch('populi.driver.request')
    def test_initialize_can_initialize_curl_options(self, mock_request):
        bio = BytesIO()
        bio.write(b'<?xml version="1.0" encoding="ISO-8859-1"?><xml><a>hi</a></xml>')
        bio.seek(0)
        mock_request.return_value = bio

        driver.driver.initialize(endpoint='whatever', access_key='access_key', curl_options=[('a', 1), ('c', 3)])

        driver.driver.call_populi({'a': 'b'})

        mock_request.assert_called_once_with(
            'whatever',
            {'a': 'b', 'access_key': 'access_key'},
            curl_options = [('a', 1), ('c', 3)])

    @patch('populi.driver.request')
    def test_call_populi(self, mock_request):
        bio = BytesIO()
        bio.write(b'<?xml version="1.0" encoding="ISO-8859-1"?><xml><a>hi</a></xml>')
        bio.seek(0)
        mock_request.return_value = bio
        driver.driver.access_key = 'override'
        driver.driver.endpoint = 'endpoint'

        (result_byte, result_xml) = driver.driver.call_populi({'a': 'b'})

        mock_request.assert_called_once_with(
            driver.driver.endpoint,
            {'a': 'b', 'access_key': driver.driver.access_key},
            curl_options=driver.driver.curl_options
        )

        self.assertEqual(result_byte, bio)

    @patch('populi.driver.request')
    def test_call_populi_raises_authentication_error(self, mock_request):
        bio = BytesIO()
        bio.write(b'<?xml version="1.0" encoding="ISO-8859-1"?><error><code>AUTHENTICATION_ERROR</code><message>Malformed access key</message></error>')
        bio.seek(0)
        mock_request.return_value = bio
        driver.driver.access_key = 'override'
        driver.driver.endpoint = 'endpoint'

        try:
            driver.driver.call_populi({'a': 'b'})
            self.assertTrue(False, 'Should have raised AuthenticationError')
        except exceptions.AuthenticationError as e:
            self.assertEqual('Malformed access key', str(e))

    @patch('populi.driver.request')
    def test_call_populi_for_raw_data(self, mock_request):
        bio = BytesIO()
        bio.write(b'HELLO WORLD')
        bio.seek(0)
        mock_request.return_value = bio
        driver.driver.access_key = 'override'
        driver.driver.endpoint = 'endpoint'

        raw_data, other = driver.driver.call_populi({'a': 'b'}, raw_data=True)
        self.assertEqual(b'HELLO WORLD', raw_data.read())
        self.assertEqual(None, other)

    @patch('populi.driver.request')
    def test_call_populi_raises_unknown_task(self, mock_request):
        bio = BytesIO()
        bio.write(b'<?xml version="1.0" encoding="ISO-8859-1"?><error><code>UNKNOWN_TASK</code><message>Unknown Task</message></error>')
        bio.seek(0)
        mock_request.return_value = bio
        driver.driver.access_key = 'override'
        driver.driver.endpoint = 'endpoint'

        try:
            driver.driver.call_populi({'a': 'b'})
            self.assertTrue(False, 'Should have raised UnknownTask')
        except exceptions.UnknownTask as e:
            self.assertEqual('Unknown Task', str(e))

    @patch('populi.driver.request')
    def test_call_populi_raises_other_when_unknown(self, mock_request):
        bio = BytesIO()
        bio.write(b'<?xml version="1.0" encoding="ISO-8859-1"?><error><code>WHATEVER_TASK</code><message>Unknown Task</message></error>')
        bio.seek(0)
        mock_request.return_value = bio
        driver.driver.access_key = 'override'
        driver.driver.endpoint = 'endpoint'

        try:
            driver.driver.call_populi({'a': 'b'})
            self.assertTrue(False, 'Should have raised Other Error')
        except exceptions.OtherError as e:
            self.assertEqual('Unknown Task', str(e))

    @patch('populi.driver.driver.call_populi')
    def test_get_all_anonymous_returns_correct_encoding(self, mock_call_populi):
        xml_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                     "data/test.xml")
        xml = etree.parse(xml_file_path).getroot()
        mock_call_populi.return_value = (None, xml)
        driver.initialize(endpoint='whatever', access_key='access_key', curl_options=[('a', 1), ('c', 3)])

        result = driver.get_all_anonymous('task', 'transaction')

        self.assertEqual(etree.tostring(xml, xml_declaration=True, encoding='UTF-8').decode('UTF-8'), result)


if __name__ == '__main__':
    unittest.main()
