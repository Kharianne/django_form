import requests as r
from xml.etree import ElementTree
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_ico(ico: (str, int)):
    """
    Validates ICO against ARES
    :param ico: int
    :return: boolean value
    """
    not_valid_error = ValidationError(_('%(value)s není validní IČO'),
                            params={'value': ico},)

    connection_error = ValidationError(_('Nemohli jsme se připojit k'
                                         'databázi ARES, zkuste to'
                                         'prosím později. Děkujeme'))

    # We don't have to spam ARES servers if we don't have an integer
    try:
        int(ico)
    except ValueError:
        raise not_valid_error

    namespaces = {
        'are': "http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_answer/v_1.0.1"
    }
    response = r.get(f"http://wwwinfo.mfcr.cz/cgi-bin/ares/darv_std.cgi?ico={ico}&aktivni=true")
    if response.status_code == 200:
        tree = ElementTree.fromstring(response.content)
        number_of_records = tree.find("are:Odpoved/are:Pocet_zaznamu", namespaces).text
        try:
            if int(number_of_records) == 0:
                raise not_valid_error
        except ValueError:
            raise not_valid_error
    else:
        raise connection_error
