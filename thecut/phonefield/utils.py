# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import phonenumbers


def format_for_display(value, region=None):
    try:
        phonenumber = phonenumbers.parse(value, region)
    except phonenumbers.NumberParseException:
        # For historical data that may not be parseable
        return value

    if region is not None and phonenumbers.is_valid_number_for_region(
            phonenumber, region):
        return phonenumbers.format_number(
            phonenumber, phonenumbers.PhoneNumberFormat.NATIONAL)
    else:
        return phonenumbers.format_number(
            phonenumber, phonenumbers.PhoneNumberFormat.INTERNATIONAL)


def format_for_uri(value):
    try:
        phonenumber = phonenumbers.parse(value, None)
    except phonenumbers.NumberParseException:
        # For historical data that may not be parseable
        return value

    return phonenumbers.format_number(
        phonenumber, phonenumbers.PhoneNumberFormat.RFC3966)
