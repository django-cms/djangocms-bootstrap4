# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='iconset_from_class')
@stringfilter
def iconset_from_class(value):
    """
    extracts the iconset from a class definition
    "fa-flask" -> "fa"
    :param value:
    :return:
    """
    if '-' in value:
        return value.split('-')[0]
    return ''
