# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


NAV_ALIGNMENT = (
    ('nav-fill', _('Fill')),
    ('nav-justified', _('Justified')),
    ('justify-content-start', _('Justify start')),
    ('justify-content-center', _('Justify center')),
    ('justify-content-end', _('Justify end')),
    ('flex-column', _('Column')),
)

NAV_STYLES = (
    ('nav-tabs', _('Tabs')),
    ('nav-pills', _('Pills')),
)
