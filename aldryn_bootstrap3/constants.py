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
    ('', 'Default',),
    ('sm', 'Small',),
    ('xs', 'Extra Small',),
)

SIZE_DEFAULT = ''


BREAKPOINTS_CHOICES = (
    ('xs', _("Tiny (<{sm[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
    ('sm', _("Small (≥{sm[0]}px and <{md[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
    ('md', _("Medium (≥{md[0]}px and <{lg[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
    ('lg', _("Large (≥{lg[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
)
BREAKPOINTS_DEFAULT = 'xs,sm,md,lg'
