# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms import TextInput


class PhoneInput(TextInput):

    input_type = 'tel'

    def __init__(self, *args, **kwargs):
        super(PhoneInput, self).__init__(*args, **kwargs)
        self.attrs.update({'autocomplete': 'tel'})
