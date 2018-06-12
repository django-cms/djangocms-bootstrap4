# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


CODE_TYPE_CHOICES = (
    ('code', _('Inline code')),
    ('pre', _('Code block')),
    ('var', _('Variables')),
    ('kbd', _('User input')),
    ('samp', _('Sample output')),
)
