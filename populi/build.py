import pycurl
from io import BytesIO
from lxml import etree
from re import sub
from bs4 import BeautifulSoup
'''
This is a utility for building the command list from the populi api webpage.
'''
api_reference_url = "https://support.populiweb.com/hc/en-us/articles/223798747-API-Reference"
root_elements = {
    'getEntriesForAccount': "ledger_entry",
    'getInvoices': "invoice",
    'getStudentBalances': "student_balance",
    'getTermStudents': "student",
    'getTransactions': "transaction",
    'getPendingCharges': "pending_charge",
    'getRoleMembers': 'person',
    'getTaggedPeople': 'person',
    'getTodos': 'todo',
    'getVoidedTransactions': 'transaction',
    'getOrganizations': 'organization',
}

raw_elements = {'downloadFile', 'downloadBackup', 'downloadStudentSchedule'}

imports = "from .driver import initialize, get_anonymous, get_all_anonymous\n\n\n"


class Command(object):
    def __init__(self, name, comment, parameters):
        self.name = name
        self.comment = comment
        self.parameters = parameters

    def paging(self):
        return next((True for p in self.parameters if p.field == 'page'), False)

    def __str__(self):
        template = '''def {}({}):
    """
    {}
    {}
    :returns: String containing xml or an lxml element.
    """
    
    return get_{}anonymous('{}'{})'''
        passing = ", ".join(["{}={}".format(p.field, p.field) for p in self.parameters if p.field != 'page'])

        if self.name in raw_elements:
            passing = f"raw_data=True, {passing}" if passing else "raw_data=True"

        if self.paging():
            if passing:
                passing = "root_element='{}', {}".format(root_elements[self.name], passing)
            else:
                passing = "root_element='{}'".format(root_elements[self.name])

        return template.format(
            sub(r'([A-Z])', r'_\1', self.name).lower(),
            ", ".join(["{}: {}={}".format(p.field, 'list' if p.default == '[]' else 'str', p.default) for p in self.parameters if p.field != 'page']),
            self.comment,
            "".join(["\n    :param {}: {}".format(p.field, p.comment) for p in self.parameters if p.field != 'page']),
            "all_" if self.paging() else "",
            self.name,
            ", {}".format(passing) if len(passing) else '')


def request_api_reference():
    curl = pycurl.Curl()
    buffer = BytesIO()

    curl.setopt(pycurl.URL, api_reference_url)
    curl.setopt(pycurl.WRITEDATA, buffer)
    curl.perform()
    curl.close()

    buffer.seek(0)

    return etree.parse(buffer, etree.HTMLParser()).getroot()


def get_commands():
    tree = request_api_reference()

    commands = []
    for i in tree.xpath('//h2'):
        command = Command(i.xpath('string()'),
                          i.getnext().xpath('string()'),
                          get_command_parameters(tree, i.xpath('string()')))
        commands.append(command)

    return commands


def get_command_parameters(tree, cmd):

    xpath = "//h2[text()='{}'][1]".format(cmd)
    header = tree.xpath(xpath)[0]
    xpath = "{}/following-sibling::h3[text()='Parameters'][1]".format(xpath)
    parameters = tree.xpath(xpath)[0]
    check = parameters.xpath(".//preceding-sibling::h2[1]")[0]

    if check is not header:
        return []

    parameters = parameters.getnext().xpath("./tbody//td")

    ps = []
    fields = []

    for i in range(0, len(parameters), 3):
        try:
            field = BeautifulSoup(parameters[i].text, 'html.parser').get_text().strip()
        except TypeError:
            continue

        if not field:
            continue

        field = field.split()[0]

        p = type('', (), {})
        p.field = field[:-2] if field[-2:] == '[]' else field
        if p.field in fields:
            continue
        fields.append(p.field)
        p.comment = parameters[i+1].text
        p.required = False if parameters[i+2].text == 'No' else True
        p.default = 'None' if p.field == field else '[]'
        ps.append(p)

    return ps
