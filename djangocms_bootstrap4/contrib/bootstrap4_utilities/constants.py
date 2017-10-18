# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


SPACER_PROPERTIES = (
    ('m', 'margin'),
    ('p', 'padding'),
)

SPACER_SIDES = (
    ('', '*'),
    ('t', '*-top'),
    ('r', '*-right'),
    ('b', '*-bottom'),
    ('l', '*-left'),
    ('x', '*-left & *-right'),
    ('y', '*-top & *-bottom'),
)

SPACER_SIZES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_SPACER_SIZES',
    (
        ('0', '* 0'),
        ('1', '* .25'),
        ('2', '* .5'),
        ('3', '* 1'),
        ('4', '* 1.5'),
        ('5', '* 3'),
    ),
)
