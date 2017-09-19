# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase

from .models import Bootstrap4GridContainer


class Bootstrap4GridContainerPlugin(CMSPluginBase):
    """
    Layout > Grid: "Container" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    model = Bootstrap4GridContainer
    name = _('Grid - Container')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/plugins/grid_container.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'container_type',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]

    def clean(self):
        # TODO clean class from attributes and attach to container
        pass


class Bootstrap4GridRowPlugin:
    pass


class Bootstrap4GridColumnPlugin:
    pass
