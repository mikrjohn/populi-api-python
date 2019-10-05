from nose.tools import *
import unittest
from unittest.mock import call, patch, MagicMock
from io import BytesIO
from urllib.parse import urlencode

from populi import driver


class TestDriver(unittest.TestCase):

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

    @patch('populi.driver.request')
    def test_call_populi(self, mock_request):
        bio = BytesIO()
        bio.write(b'<?xml version="1.0" encoding="ISO-8859-1"?><xml><a>hi</a></xml>')
        bio.seek(0)
        mock_request.return_value = bio
        driver.driver.access_key = 'override'
        driver.driver.endpoint = 'endpoint'

        result = driver.driver.call_populi({'a': 'b'})

        mock_request.called_once_with(driver.driver.endpoint,
            {'a': 'b', 'access_key': driver.driver.endpoint})

        self.assertEqual(result, bio)


if __name__ == '__main__':
    unittest.main()
