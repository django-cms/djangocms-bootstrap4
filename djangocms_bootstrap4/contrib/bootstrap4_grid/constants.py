# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# The default grid size for Bootstrap 4 is 12. You can change this setting
# to whatever layout you require. We suggest that the value is at
# least devisable by 2, 3 and 4.
GRID_SIZE = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_SIZE',
    12,
)

# Bootstrap 4 provides 2 container types, .container and .container-fluid
# https://getbootstrap.com/docs/4.0/layout/grid/#no-gutters
GRID_CONTAINER_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS',
    (
        ('container', _('Container')),
        ('container-fluid', _('Fluid container')),
    ),
)

# Options for flexbox on the alignment of the grid
# https://flexbox.webflow.com/
GRID_ROW_VERTICAL_ALIGNMENT_CHOICES = (
    ('align-items-start', _('Align items start')),
    ('align-items-center', _('Align items center')),
    ('align-items-end', _('Align items end')),
)

GRID_ROW_HORIZONTAL_ALIGNMENT_CHOICES = (
    ('justify-content-start', _('Justify content start')),
    ('justify-content-center', _('Justify content center')),
    ('justify-content-end', _('Justify content end')),
    ('justify-content-around', _('Justify content around')),
    ('justify-content-between', _('Justify content between')),
)

GRID_COLUMN_ALIGNMENT_CHOICES = (
    ('align-self-start', _('Align self start')),
    ('align-self-center', _('Align self center')),
    ('align-self-end', _('Align self end')),
)

GRID_COLUMN_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES',
    (
        ('col', _('Column')),
        ('w-100', _('Break')),
        ('', _('Empty'))
    ),
)
