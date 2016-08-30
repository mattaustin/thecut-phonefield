# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import forms, validators
from django.core.exceptions import ValidationError
from django.db.models import CharField
import phonenumbers


class PhoneNumberField(CharField):

    default_error_messages = {
        'invalid': '\'%(value)s\' is an invalid phone number.'
    }

    default_validators = []

    description = 'Phone number'

    phone_number_format = phonenumbers.PhoneNumberFormat.INTERNATIONAL

    phone_number_region = None

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        phone_number_format = kwargs.pop('format', None)
        phone_number_region = kwargs.pop('region', None)

        if phone_number_format is not None:
            self.phone_number_format = phone_number_format
        if phone_number_region is not None:
            self.phone_number_region = phone_number_region

        if not self.default_validators:
            self.default_validators = [
                validators.PhoneNumberValidator(
                    region=self.phone_number_region)]

        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def deconstruct(self, *args, **kwargs):
        name, path, args, kwargs = super(PhoneNumberField, self).deconstruct()
        del kwargs['max_length']
        if self.phone_number_format != self.__class__.phone_number_format:
            kwargs['format'] = self.phone_number_format
        if self.phone_number_region != self.__class__.phone_number_region:
            kwargs['region'] = self.phone_number_region
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.PhoneNumberField,
                    'format': self.phone_number_format,
                    'region': self.phone_number_region}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)

    def from_db_value(self, value, *args, **kwargs):
        return self.to_python(value)

    def get_prep_value(self, value):
        return self.to_python(value)

    def to_python(self, value):
        if value in self.empty_values:
            return ''
        try:
            value = phonenumbers.parse(value, self.phone_number_region)
        except phonenumbers.NumberParseException:
            raise ValidationError(self.error_messages['invalid'],
                                  code='invalid', params={'value': value})
        value = phonenumbers.format_number(value, self.phone_number_format)
        return value.replace(' ', '')
