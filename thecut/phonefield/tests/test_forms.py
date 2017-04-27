# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
from thecut.phonefield.forms import AUPhoneNumberField, PhoneNumberField
from thecut.phonefield.validators import PhoneNumberValidator
from django.forms import CharField


try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


class TestAUPhoneNumberField(TestCase):
    def test_au_phone_field(self):
        f = AUPhoneNumberField()
        self.assertEqual(len(f.validators), 1)
        self.assertEqual(type(f.validators[0]), PhoneNumberValidator)
        self.assertEqual(f.validators[0].region, 'AU')

    def test_field_initialisation(self):
        f = PhoneNumberField(format='FORMAT', placeholder='PLACEHOLDER',
                             region='UK')
        self.assertEqual(f.phone_number_format, 'FORMAT')
        self.assertEqual(f.phone_number_placeholder, 'PLACEHOLDER')
        self.assertEqual(f.phone_number_region, 'UK')
        self.assertEqual(len(f.validators), 1)
        self.assertEqual(type(f.validators[0]), PhoneNumberValidator)
        self.assertEqual(f.validators[0].region, 'UK')

    @mock.patch.object(CharField, 'clean')
    def test_clean_empty(self, mock_clean):
        mock_clean.return_value = ''
        f = PhoneNumberField()
        self.assertEqual(f.clean(), '')

    @mock.patch.object(CharField, 'clean')
    def test_clean_valid_phone(self, mock_clean):
        mock_clean.return_value = '0894051234'
        f = PhoneNumberField(region='AU')
        self.assertEqual(f.clean(), '+61894051234')

    def test_prepare_value(self):
        f = PhoneNumberField(region='AU')
        self.assertEqual(f.prepare_value('+61894051234'), '(08) 9405 1234')

