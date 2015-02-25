# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _
from .conf import settings

CONTEXT_CHOICES = (
    ('default', 'Default',),
    ('primary', 'Primary',),
    ('success', 'Success',),
    ('info', 'Info',),
    ('warning', 'Warning',),
    ('danger', 'Danger',),
)
CONTEXT_DEFAULT = 'default'

BUTTON_CONTEXT_CHOICES = CONTEXT_CHOICES + (
    ('link', 'Link',),
)
BUTTON_CONTEXT_DEFAULT = 'default'

SIZE_CHOICES = (
    ('lg', 'Large',),
    ('md', 'Medium',),
    ('sm', 'Small',),
    ('xs', 'Extra Small',),
)

SIZES = tuple([size for size, name in SIZE_CHOICES])

SIZE_DEFAULT = 'md'


BREAKPOINTS = {
    'lg': (1200, 'desktop', _("large desktops"), 1170),
    'md': (992, 'laptop', _("laptops"), 970),
    'sm': (768, 'tablet', _("tablets"), 750),
    'xs': (768, 'mobile-phone', _("mobile phones"), 750),
}


# WARNING: changing DEVICE_CHOICES will cause model creation to change and requires database migrations!
DEVICE_CHOICES = (
    ('xs', _("Tiny (<{sm[0]}px)".format(**BREAKPOINTS))),
    ('sm', _("Small (≥{sm[0]}px and <{md[0]}px)".format(**BREAKPOINTS))),
    ('md', _("Medium (≥{md[0]}px and <{lg[0]}px)".format(**BREAKPOINTS))),
    ('lg', _("Large (≥{lg[0]}px)".format(**BREAKPOINTS))),
)
DEVICE_SIZES = tuple([size for size, name in DEVICE_CHOICES])

GRID_SIZE = settings.ALDRYN_BOOTSTRAP3_GRID_SIZE
