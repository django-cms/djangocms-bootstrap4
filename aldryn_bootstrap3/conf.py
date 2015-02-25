# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from appconf import AppConf


class AldrynSitesConf(AppConf):
    BREAKPOINTS = {
        'lg': (1200, 'desktop', _("large desktops"), 1170),
        'md': (992, 'laptop', _("laptops"), 970),
        'sm': (768, 'tablet', _("tablets"), 750),
        'xs': (768, 'mobile-phone', _("mobile phones"), 750),
    }
    GRID_COLUMNS = 24
