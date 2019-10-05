from nose.tools import *
import unittest
import pycurl
from io import BytesIO
from lxml import etree, html
from re import sub

import populi


class TestPopuli(unittest.TestCase):
    def test_can_initialize(self):
        self.assertTrue(hasattr(populi, 'initialize'))

    def test_all_current_cmds_exist(self):
        api_reference_url = "https://support.populiweb.com/hc/en-us/articles/223798747-API-Reference"
        curl = pycurl.Curl()
        buffer = BytesIO()

        curl.setopt(pycurl.URL, api_reference_url)
        curl.setopt(pycurl.WRITEDATA, buffer)
        curl.perform()
        curl.close()

        buffer.seek(0)

        xml = etree.parse(buffer, etree.HTMLParser()).getroot()

        self.assertGreater(len(xml.xpath('//h2')), 10)

        for cmd in xml.xpath('//h2/text()'):
            cmd = sub(r'([A-Z])', r'_\1', cmd).lower()
            self.assertTrue(hasattr(populi, cmd), "Missing {} Cmd. Rebuild required.".format(cmd))

if __name__ == '__main__':
    unittest.main()
