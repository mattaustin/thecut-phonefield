# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .. import utils
from django import template


register = template.Library()


@register.filter(name='au_phone_number')
def au_phone_number(value):
    return utils.format_for_display(value, region='AU')
