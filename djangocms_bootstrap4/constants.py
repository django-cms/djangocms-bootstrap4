# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from .conf import settings


DEVICE_CHOICES = (
    ('xs', _('Extra small')),   # default <576px
    ('sm', _('Small')),         # default ≥576px
    ('md', _('Medium')),        # default ≥768px
    ('lg', _('Large')),         # default ≥992px
    ('xl', _('Extra large')),   # default ≥1200px
)

DEVICE_SIZES = tuple([size for size, name in DEVICE_CHOICES])

TARGET_CHOICES = (
    ('_blank', _('Open in new window')),
    ('_self', _('Open in same window')),
    ('_parent', _('Delegate to parent')),
    ('_top', _('Delegate to top')),
)

CONTEXT_CHOICES = (
    ('primary', _('Primary'),),
    ('success', _('Success'),),
    ('info', _('Info'),),
    ('warning', _('Warning'),),
    ('danger', _('Danger'),),
)

CONTEXT_DEFAULT = 'default'
