# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text
import phonenumbers
import warnings


class PhoneNumberValidator(object):

    message = 'Enter a valid {region} phone number. Please ensure the full ' \
              'phone number is provided.'

    region = None

    def __init__(self, region=None, message=None):
        if region is not None:
            self.region = region
        if message is not None:
            self.message = message

    def __call__(self, value):
        value = force_text(value)
        try:
            phonenumber = phonenumbers.parse(value, region=self.region)
        except phonenumbers.NumberParseException:
            raise ValidationError(self.get_message())
        if not phonenumbers.is_valid_number(phonenumber):
            raise ValidationError(self.get_message())

    def get_message(self):
        return self.message.format(
            region=self.region if self.region else 'international')


# Deprecated

class AUPhoneNumberValidator(PhoneNumberValidator):

    message = 'Enter a valid Australian phone number. Please ensure the ' \
              'full phone number is provided.'

    region = 'AU'

    def __call__(self, *args, **kwargs):
        warnings.warn(
            'AUPhoneNumberValidator is deprecated, use '
            'PhoneNumberValidator(region=\'AU\') instead.',
            DeprecationWarning, stacklevel=2)
        return super(AUPhoneNumberValidator, self).__call__(*args, **kwargs)

validate_auphonenumber = AUPhoneNumberValidator()
