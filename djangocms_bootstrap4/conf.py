# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class AldrynSitesConf(AppConf):
    GRID_SIZE = 24
    ICONSETS = (
        # NOTE: these values are overridden by the settings from aldryn_config.py on aldryn
        # first value is the iconset identifier for http://victor-valencia.github.io/bootstrap-iconpicker/
        # second is the prefix for the css class
        # third is the pretty name shown in the select box
        ('glyphicons', 'glyphicons', 'Glyphicons'),
        ('fontawesome', 'fa', 'Fontawesome'),
    )
