# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text
import phonenumbers


class AUPhoneNumberValidator(object):

    invalid_message = 'Invalid Australian phone number. Please ensure full ' \
                      'phone number is provided.'

    def __call__(self, value):
        value = force_text(value)
        try:
            phonenumber = phonenumbers.parse(value, region='AU')
        except phonenumbers.NumberParseException:
            raise ValidationError(self.invalid_message)
        if not phonenumbers.is_valid_number(phonenumber):
            raise ValidationError(self.invalid_message)


validate_auphonenumber = AUPhoneNumberValidator()
