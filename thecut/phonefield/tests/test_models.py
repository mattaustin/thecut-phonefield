# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .. import models
from django.core.exceptions import ValidationError
from django.utils import six
from unittest import TestCase


try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


class TestPhoneNumberField(TestCase):

    def setUp(self):
        self.field = models.PhoneNumberField(region='AU')

    def test_from_db_value_calls_to_python_with_provided_value(self):
        value = 'TEST_VALUE'
        with mock.patch.object(self.field, 'to_python') as to_python:
            self.field.from_db_value(value)

        self.assertTrue(to_python.called)
        to_python.assert_called_with(value)

    def test_to_python_returns_text(self):

        self.assertEqual(six.text_type, type(self.field.to_python('+44100')))

    def test_to_python_returns_empty_string_when_given_none(self):

        self.assertEqual('', self.field.to_python(None))

    def test_to_python_returns_empty_string_when_given_an_empty_string(self):

        self.assertEqual('', self.field.to_python(''))

    def test_to_python_raises_validationerror_when_given_an_invalid_string(self):  # NOQA

        self.assertRaises(ValidationError, self.field.to_python, 'INVALID')

    def test_setting_phone_number_format(self):
        f = models.PhoneNumberField(format='FORMAT')
        self.assertEqual(f.phone_number_format, 'FORMAT')
