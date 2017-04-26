# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
import phonenumbers
from thecut.phonefield.utils import format_for_display


try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


class TestFormatForDisplay(TestCase):
    @mock.patch('phonenumbers.parse')
    def test_number_parse_exception(self, mock_parse):
        mock_parse.side_effect = phonenumbers.NumberParseException(
            'Test error', 'Test error')
        phone1 = 'blahblah'
        phone2 = format_for_display(phone1, 'AU')
        self.assertIs(phone1, phone2)

    @mock.patch('phonenumbers.format_number')
    def test_phone_valid_for_this_region(self, mock_format_number):
        format_for_display('08 9405 1234', 'AU')
        (number, phone_number_format) = mock_format_number.call_args[0]
        self.assertEqual(phone_number_format,
                         phonenumbers.PhoneNumberFormat.NATIONAL)

    @mock.patch('phonenumbers.format_number')
    def test_phone_invalid_for_this_region(self, mock_format_number):
        format_for_display('+1-510-748-8230', 'AU')
        (number, phone_number_format) = mock_format_number.call_args[0]
        self.assertEqual(phone_number_format,
                         phonenumbers.PhoneNumberFormat.INTERNATIONAL)
