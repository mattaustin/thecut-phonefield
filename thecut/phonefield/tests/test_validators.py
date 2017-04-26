# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
from thecut.phonefield.validators import PhoneNumberValidator


try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


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
