# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import utils, validators, widgets
from django.core.validators import EMPTY_VALUES
from django.forms import CharField
import phonenumbers
import re


class AUPhoneNumberField(CharField):

    default_validators = [validators.validate_auphonenumber]

    phone_number_format = phonenumbers.PhoneNumberFormat.INTERNATIONAL

    phone_number_placeholder = '(xx) xxxx xxxx'

    phone_number_region = 'AU'

    widget = widgets.PhoneInput

    def clean(self, *args, **kwargs):
        value = super(AUPhoneNumberField, self).clean(*args, **kwargs)
        if value in EMPTY_VALUES:
            return ''

        value = phonenumbers.parse(value, self.phone_number_region)
        value = phonenumbers.format_number(value, self.phone_number_format)
        return re.sub(r'[^+\d+]+', '', value)

    def prepare_value(self, value):
        return utils.format_for_display(value, self.phone_number_region)

    def widget_attrs(self, *args, **kwargs):
        widget_attrs = super(AUPhoneNumberField, self).widget_attrs(*args,
                                                                    **kwargs)
        widget_attrs.setdefault('placeholder', self.phone_number_placeholder)
        return widget_attrs
