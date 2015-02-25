# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

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
