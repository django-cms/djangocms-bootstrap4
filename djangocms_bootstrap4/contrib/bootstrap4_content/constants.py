# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


CODE_TYPE_CHOICES = (
    ('code', _('Inline code')),
    ('pre', _('Code block')),
    ('var', _('Variables')),
    ('kbd', _('User input')),
    ('samp', _('Sample output')),
)

QUOTE_ALIGN_CHOICES = (
    ('', _('Left')),
    ('text-center', _('Center')),
    ('text-right', _('Right')),
)
