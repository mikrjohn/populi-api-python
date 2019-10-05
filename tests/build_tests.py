from nose.tools import *
import unittest
import pycurl
from io import BytesIO
from unittest.mock import call, patch, MagicMock
from lxml import etree

from populi import build



class TestPopuliBuild(unittest.TestCase):

    @patch('populi.build.BytesIO')
    @patch('populi.build.pycurl')
    def test_get_api_reference(self, mock_pycurl, mock_BytesIO):
        curl = MagicMock()
        mock_pycurl.Curl.return_value = curl
        mock_pycurl.URL = 'blah'
        mock_pycurl.WRITEDATA = 'blimp'

        bio = BytesIO()
        expected_html = b'<html><body><p>Test</p></body></html>'
        bio.write(expected_html)
        mock_BytesIO.return_value = bio

        response = build.request_api_reference()

        calls = [call('blah', build.api_reference_url), call('blimp', bio)]

        curl.setopt.assert_has_calls(calls, any_order=True)
        curl.perform.assert_called_once_with()
        curl.close.assert_called_once_with()

        self.assertEqual(type(response), etree._Element)
        self.assertEqual(expected_html, etree.tostring(response))

    def test_get_none_command_parameters(self):
        html = b'''<html><body>
                <h2><a id="getPayment"></a>getPayment</h2>
                <p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
                <h3>Parameters</h3>
                <p>None.</p>
                </body></html>'''
        tree = etree.fromstring(html, etree.HTMLParser())

        parameters = build.get_command_parameters(tree, 'getPayment')

        self.assertEqual(len(parameters), 0)

    def test_no_parameters_exist(self):
        html = b'''<html><body>
        <h2><a id="getPayment"></a>getPayment</h2>
        <p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
        <h2><a id="getWhatever"></a>getWhatever</h2>
        <p>Blah blah blah</p>
        <h3>Parameters</h3>
        <table style="width: 100%; border: 1px solid #767676;" border="0">
        <thead>
        <tr style="background-color: #eee;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Required</td>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>payment_id</td>
        <td>The numeric ID of the payment you're interested in.</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>student_id</td>
        <td>The numeric ID of the student.</td>
        <td>No</td>
        </tr>
        </tbody>
        </table>
        </body></html>'''
        tree = etree.fromstring(html, etree.HTMLParser())

        parameters = build.get_command_parameters(tree, 'getPayment')

        self.assertEqual(len(parameters), 0)

    def test_get_single_command_parameter(self):
        html = b'''<html><body>
        <h2><a id="getPayment"></a>getPayment</h2>
        <p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
        <h3>Parameters</h3>
        <table style="width: 100%; border: 1px solid #767676;" border="0">
        <thead>
        <tr style="background-color: #eee;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Required</td>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>payment_id</td>
        <td>The numeric ID of the payment you're interested in.</td>
        <td>Yes</td>
        </tr>
        </tbody>
        </table>
        </body></html>'''
        tree = etree.fromstring(html, etree.HTMLParser())

        parameters = build.get_command_parameters(tree, 'getPayment')

        self.assertEqual(len(parameters), 1)
        self.assertEqual(parameters[0].field, 'payment_id')
        self.assertEqual(parameters[0].comment, 'The numeric ID of the payment you\'re interested in.')
        self.assertEqual(parameters[0].required, True)

    def test_get_single_command_parameter_w_extra_junk(self):
        html = b'''<html><body>
        <h2><a id="getPayment"></a>getPayment</h2>
        <p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
        <h3>Parameters</h3>
        <table style="width: 100%; border: 1px solid #767676;" border="0">
        <thead>
        <tr style="background-color: #eee;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Required</td>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>payment_id blah blah blah</td>
        <td>The numeric ID of the payment you're interested in.</td>
        <td>Yes</td>
        </tr>
        </tbody>
        </table>
        </body></html>'''
        tree = etree.fromstring(html, etree.HTMLParser())

        parameters = build.get_command_parameters(tree, 'getPayment')

        self.assertEqual(len(parameters), 1)
        self.assertEqual(parameters[0].field, 'payment_id')
        self.assertEqual(parameters[0].comment, 'The numeric ID of the payment you\'re interested in.')
        self.assertEqual(parameters[0].required, True)

    def test_get_double_command_parameter(self):
        html = b'''<html><body>
        <h2><a id="getPayment"></a>getPayment</h2>
        <p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
        <h3>Parameters</h3>
        <table style="width: 100%; border: 1px solid #767676;" border="0">
        <thead>
        <tr style="background-color: #eee;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Required</td>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>payment_id</td>
        <td>The numeric ID of the payment you're interested in.</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>student_id</td>
        <td>The numeric ID of the student.</td>
        <td>No</td>
        </tr>
        </tbody>
        </table>
        </body></html>'''
        tree = etree.fromstring(html, etree.HTMLParser())


        parameters = build.get_command_parameters(tree, 'getPayment')

        self.assertEqual(len(parameters), 2)

        self.assertEqual(parameters[0].field, 'payment_id')
        self.assertEqual(parameters[0].comment, 'The numeric ID of the payment you\'re interested in.')
        self.assertEqual(parameters[0].required, True)

        self.assertEqual(parameters[1].field, 'student_id')
        self.assertEqual(parameters[1].comment, 'The numeric ID of the student.')
        self.assertEqual(parameters[1].required, False)

    def test_get_parameters_where_some_parameters_repeat(self):
        html = b'''<html><body>
        <h2><a id="getPayment"></a>getPayment</h2>
        <p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
        <h3>Parameters</h3>
        <table style="width: 100%; border: 1px solid #767676;" border="0">
        <thead>
        <tr style="background-color: #eee;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Required</td>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>student_id</td>
        <td>The numeric ID of the payment you're interested in.</td>
        <td>Yes</td>
        </tr>
        <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><td></td><td>whatever</td><td>huh</td></tr>
        <tr>
        <td>student_id</td>
        <td>The numeric ID of the student.</td>
        <td>No</td>
        </tr>
        </tbody>
        </table>
        </body></html>'''

        tree = etree.fromstring(html, etree.HTMLParser())

        parameters = build.get_command_parameters(tree, 'getPayment')

        self.assertEqual(len(parameters), 1)

        self.assertEqual(parameters[0].field, 'student_id')

    def test_get_parameters_where_some_rows_are_blank(self):
        html = b'''<html><body>
        <h2><a id="getPayment"></a>getPayment</h2>
        <p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
        <h3>Parameters</h3>
        <table style="width: 100%; border: 1px solid #767676;" border="0">
        <thead>
        <tr style="background-color: #eee;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Required</td>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>payment_id</td>
        <td>The numeric ID of the payment you're interested in.</td>
        <td>Yes</td>
        </tr>
        <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><td></td><td>whatever</td><td>huh</td></tr>
        <tr>
        <td>student_id</td>
        <td>The numeric ID of the student.</td>
        <td>No</td>
        </tr>
        </tbody>
        </table>
        </body></html>'''
        tree = etree.fromstring(html, etree.HTMLParser())

        parameters = build.get_command_parameters(tree, 'getPayment')

        self.assertEqual(len(parameters), 2)

        self.assertEqual(parameters[0].field, 'payment_id')

        self.assertEqual(parameters[1].field, 'student_id')

    @patch('populi.build.request_api_reference')
    def test_get_commands(self, mock_api_ref):
        html = b'''<html><body>
<h2><a id="getPayment"></a>getPayment</h2>
<p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
<h3>Parameters</h3>
<table style="width: 100%; border: 1px solid #767676;" border="0">
<thead>
<tr style="background-color: #eee;">
<td>Parameter</td>
<td>Description</td>
<td>Required</td>
</tr>
</thead>
<tbody>
<tr>
<td>payment_id</td>
<td>The numeric ID of the payment you're interested in.</td>
<td>Yes</td>
</tr>
</tbody>
</table>
</body></html>'''
        mock_api_ref.return_value = etree.fromstring(html, etree.HTMLParser())

        commands = build.get_commands()

        self.assertEqual(len(commands), 1)
        self.assertEqual(commands[0].name, 'getPayment')
        self.assertEqual(commands[0].comment, 'Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.')
        self.assertEqual(len(commands[0].parameters), 1)
        self.assertEqual(commands[0].parameters[0].field, 'payment_id')
        self.assertEqual(commands[0].parameters[0].comment, 'The numeric ID of the payment you\'re interested in.')
        self.assertEqual(commands[0].parameters[0].required, True)
        self.assertEqual(commands[0].parameters[0].default, 'None')

    def test_command_class_paging(self):
        command = build.Command('freddy', 'fries', [])
        reg_field = type('', (), {})
        pag_field = type('', (), {})
        reg_field.field = 'whatever'
        pag_field.field = 'page'

        self.assertFalse(command.paging())

        command.parameters = [reg_field]

        self.assertFalse(command.paging())

        command.parameters = [pag_field]

        self.assertTrue(command.paging())

        command.parameters = [reg_field, pag_field]

        self.assertTrue(command.paging())

    def test_build_command_wo_arguments_string(self):
        expected_string = '''def freddy():
    """
    fries
    
    :returns: String containing xml or an lxml element.
    """
    
    return get_anonymous('freddy')'''

        command = build.Command('freddy', 'fries', [])

        result = str(command)

        self.assertEqual(expected_string, result)

    def test_build_command_w_capitalization_made_pythonic(self):
        expected_string = '''def get_freddy():
    """
    fries
    
    :returns: String containing xml or an lxml element.
    """
    
    return get_anonymous('getFreddy')'''

        command = build.Command('getFreddy', 'fries', [])

        result = str(command)

        self.assertEqual(expected_string, result)

    def test_build_command_with_paging(self):
        expected_string = '''def get_freddy():
    """
    fries
    
    :returns: String containing xml or an lxml element.
    """
    
    return get_all_anonymous('getFreddy', root_element='getFreddee')'''
        command = build.Command('getFreddy', 'fries', [])
        pag_field = type('', (), {})
        pag_field.field = 'page'
        command.parameters = [pag_field]
        build.root_elements['getFreddy'] = 'getFreddee'

        result = str(command)

        self.assertEqual(expected_string, result)
        del(build.root_elements['getFreddy'])

    def test_build_command_with_one_parameter(self):
        expected_string = '''def get_custom_field_options(custom_field_id: str=None):
    """
    Returns
    
    :param custom_field_id: Blah
    :returns: String containing xml or an lxml element.
    """
    
    return get_anonymous('getCustomFieldOptions', custom_field_id=custom_field_id)'''

        field = type('', (), {})
        field.field = 'custom_field_id'
        field.required = False
        field.default = 'None'
        field.comment = 'Blah'
        command = build.Command('getCustomFieldOptions', 'Returns', [field])

        result = str(command)

        self.assertEqual(expected_string, result)

    def test_get_command_parameter_that_is_php_array(self):
        html = b'''<html><body>
        <h2><a id="getPayment"></a>getPayment</h2>
        <p>Returns all basic and associated information about a payment. This could include credit card information, electronic check information, invoice payments, and payment refunds.</p>
        <h3>Parameters</h3>
        <table style="width: 100%; border: 1px solid #767676;" border="0">
        <thead>
        <tr style="background-color: #eee;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Required</td>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>payment_id[]</td>
        <td>The numeric ID of the payment you're interested in.</td>
        <td>Yes</td>
        </tr>
        </tbody>
        </table>
        </body></html>'''
        tree = etree.fromstring(html, etree.HTMLParser())

        parameters = build.get_command_parameters(tree, 'getPayment')

        self.assertEqual(len(parameters), 1)
        self.assertEqual(parameters[0].field, 'payment_id')
        self.assertEqual(parameters[0].comment, 'The numeric ID of the payment you\'re interested in.')
        self.assertEqual(parameters[0].required, True)
        self.assertEqual(parameters[0].default, '[]')

    def test_build_command_with_one_array_parameter(self):
        expected_string = '''def get_custom_field_options(custom_field_id: list=[]):
    """
    Returns
    
    :param custom_field_id: Blah
    :returns: String containing xml or an lxml element.
    """
    
    return get_anonymous('getCustomFieldOptions', custom_field_id=custom_field_id)'''

        field = type('', (), {})
        field.field = 'custom_field_id'
        field.required = True
        field.comment = 'Blah'
        field.default = '[]'
        command = build.Command('getCustomFieldOptions', 'Returns', [field])

        result = str(command)

        self.assertEqual(expected_string, result)
