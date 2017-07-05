# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
from thecut.phonefield.validators import PhoneNumberValidator
from django.core.exceptions import ValidationError


class TestValidatorMessage(TestCase):
    def test_no_region(self):
        v = PhoneNumberValidator()
        self.assertEqual(v.get_message(), 'Enter a valid international phone '
                         'number. Please ensure the full phone number is '
                         'provided.')

    def test_au_region(self):
        v = PhoneNumberValidator(region='AU')
        self.assertEqual(v.get_message(), 'Enter a valid AU phone '
                         'number. Please ensure the full phone number is '
                         'provided.')


class TestValidation(TestCase):
    def test_not_a_number(self):
        v = PhoneNumberValidator(region='AU')
        with self.assertRaises(ValidationError):
            v('blah')

    def test_not_valid_phone_number(self):
        v = PhoneNumberValidator(region='AU')
        with self.assertRaises(ValidationError):
            v('1223')

    def test_is_valid_phone_number(self):
        v = PhoneNumberValidator(region='AU')
        v('0894051234')
