# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from enumfields import Enum


# The default grid size for Bootstrap 4 is 12. You can change this setting
# to whatever layout you require. We suggest that the value is at
# least devisable by 2, 3 and 4.
GRID_SIZE = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_SIZE',
    12,
)


class GridContainerType(Enum):
    """
    contains css classes
    """
    DYNAMIC_WIDTH = 'container'
    FULL_WIDTH = 'container-fluid'


GRID_CONTAINER_TYPE: GridContainerType = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_TYPE',
    GridContainerType,
)


container_fieldsets_default = [
    (None, {
        'fields': (
            'name',
            'width_internal',
            'background',
            'spacing_vertical',
        ),
    }),
    (_('Advanced settings'), {
        'classes': ['collapse'],
        'fields': (
            'tag_type',
            'attributes',
        ),
    }),
]

GRID_CONTAINER_FIELDSETS = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_FIELDSETS',
    container_fieldsets_default,
)


class GridContainerWidthInternal(Enum):
    FULL_WIDTH = 'full-width'


GRID_CONTAINER_WIDTH_INTERNAL: GridContainerWidthInternal = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_WIDTH_INTERNAL',
    GridContainerWidthInternal,
)


class GridContainerBackground(Enum):
    """
    contains css classes
    """
    NONE = 'background-none'


GRID_CONTAINER_BACKGROUND: GridContainerBackground = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_BACKGROUND',
    GridContainerBackground,
)


class GridContainerSpacing(Enum):
    """
    contains css classes
    """
    NONE = 'spacing-none'


GRID_CONTAINER_SPACING: GridContainerSpacing = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINER_SPACING',
    GridContainerSpacing,
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

GRID_COLUMN_HORIZONTAL_ALIGNMENT_CHOICES = (
    ('align-items-start', _('Align items start')),
    ('align-items-center', _('Align items center')),
    ('align-items-end', _('Align items end')),
    ('align-items-stretch', _('Align items stretch')),
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


# deprecated, left only for migrations
GRID_CONTAINER_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS',
    (
        ('container', _('Container')),
        ('container-fluid', _('Fluid container')),
    ),
)
