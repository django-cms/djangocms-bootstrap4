# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


LINK_CHOICES = (
    ('link', _('Link')),
    ('btn', _('Button')),
)

LINK_SIZE_CHOICES = (
    ('btn-sm', _('Small')),
    ('', _('Medium')),
    ('btn-lg', _('Large')),
)

USE_LINK_ICONS = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_USE_ICONS',
    True,
)
