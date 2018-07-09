# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


CAROUSEL_PAUSE_CHOICES = (
    ('hover', 'hover'),
    ('mouseenter', 'mouseenter'),
    ('mouseleave', 'mouseleave'),
    ('false', 'off'),
)

CAROUSEL_RIDE_CHOICES = (
    ('carousel', 'carousel'),
    ('false', 'off'),
)

CAROUSEL_TEMPLATE_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_CAROUSEL_TEMPLATES',
    (
        ('default', _('Default')),
    ),
)

# this is used when no valua is passed in the template via
# {% with 1024 as width and 768 as height %}
CAROUSEL_DEFAULT_SIZE = [1024, 768]

CAROUSEL_ASPECT_RATIOS = (
    (1, 1),
    (3, 2),
    (4, 3),
    (21, 9),
    (18, 9),
) + tuple(
    getattr(
        settings,
        'DJANGOCMS_BOOTSTRAP4_CAROUSEL_ASPECT_RATIOS',
        tuple()
    )
)

CAROUSEL_ASPECT_RATIO_CHOICES = (
    tuple([
        ('{0}x{1}'.format(x, y), '{0}x{1}'.format(x, y))
        for x, y in CAROUSEL_ASPECT_RATIOS
    ])
)
