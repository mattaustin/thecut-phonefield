# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import utils, validators, widgets
from django.core.validators import EMPTY_VALUES
from django.forms import CharField
import phonenumbers
import re


class PhoneNumberField(CharField):

    default_validators = []

    phone_number_format = phonenumbers.PhoneNumberFormat.INTERNATIONAL

    phone_number_placeholder = '+xx...'

    phone_number_region = None

    widget = widgets.PhoneInput

    def __init__(self, *args, **kwargs):
        phone_number_format = kwargs.pop('format', None)
        phone_number_placeholder = kwargs.pop('placeholder', None)
        phone_number_region = kwargs.pop('region', None)

        if phone_number_format is not None:
            self.phone_number_format = phone_number_format
        if phone_number_placeholder is not None:
            self.phone_number_placeholder = phone_number_placeholder
        if phone_number_region is not None:
            self.phone_number_region = phone_number_region

        if not self.default_validators:
            self.default_validators = [
                validators.PhoneNumberValidator(
                    region=self.phone_number_region)]

        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        value = super(PhoneNumberField, self).clean(*args, **kwargs)
        if value in EMPTY_VALUES:
            return ''
        value = phonenumbers.parse(value, self.phone_number_region)
        value = phonenumbers.format_number(value, self.phone_number_format)
        return re.sub(r'[^+\d+]+', '', value)

    def prepare_value(self, value):
        return utils.format_for_display(value, self.phone_number_region)

    def widget_attrs(self, *args, **kwargs):
        widget_attrs = {'placeholder': self.phone_number_placeholder}
        widget_attrs.update(
            super(PhoneNumberField, self).widget_attrs(*args, **kwargs))
        return widget_attrs


class AUPhoneNumberField(PhoneNumberField):

    default_validators = [
        validators.PhoneNumberValidator(
            region='AU',
            message='Enter a valid Australian phone number. Please ensure the '
                    'full phone number is provided.')]

    phone_number_placeholder = '(xx) xxxx xxxx'

    phone_number_region = 'AU'
