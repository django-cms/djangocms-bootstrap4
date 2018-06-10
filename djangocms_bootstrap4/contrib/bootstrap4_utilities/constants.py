# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings


SPACER_PROPERTY_CHOICES = (
    ('m', 'margin'),
    ('p', 'padding'),
)

SPACER_SIDE_CHOICES = (
    ('', '*'),
    ('t', '*-top'),
    ('r', '*-right'),
    ('b', '*-bottom'),
    ('l', '*-left'),
    ('x', '*-left & *-right'),
    ('y', '*-top & *-bottom'),
)

SPACER_SIZE_CHOICES = getattr(
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
