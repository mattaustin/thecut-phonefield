# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import forms, validators
from django.db.models import CharField


class PhoneNumberField(CharField):

    default_validators = []

    description = 'Phone number'

    def __init__(self, *args, **kwargs):
        # phone_number_format = kwargs.pop('format', None)
        phone_number_region = kwargs.get('region', None)

        # if phone_number_format is not None:
        #     self.phone_number_format = phone_number_format
        if phone_number_region is not None:
            self.phone_number_region = phone_number_region

        if not self.default_validators:
            self.default_validators = [
                validators.PhoneNumberValidator(
                    region=self.phone_number_region)]

        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.PhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)
