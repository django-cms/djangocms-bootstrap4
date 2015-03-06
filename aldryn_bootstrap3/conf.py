# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from appconf import AppConf


class AldrynSitesConf(AppConf):
    GRID_SIZE = 24
    ICONSETS = (
        # http://victor-valencia.github.io/bootstrap-iconpicker/
        ('glyphicons', 'glyphicons', 'Glyphicons'),
        ('fontawesome', 'fa', 'Fontawesome'),
    )
