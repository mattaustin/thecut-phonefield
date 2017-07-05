# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .. import utils
from django import template


register = template.Library()


@register.filter(name='phone_number')
def phone_number(value, region=None):
    return utils.format_for_display(value, region)


@register.filter(name='uri_phone_number')
def uri_phone_number(value):
    return utils.format_for_uri(value)


# Deprecated - please use phone_number
@register.filter(name='au_phone_number')
def au_phone_number(value):
    return utils.format_for_display(value, region='AU')
