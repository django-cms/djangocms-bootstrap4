# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase

from .models import (
    Bootstrap4GridContainer,
    Bootstrap4GridRow,
    Bootstrap4GridColumn,
)


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
                'tag_type',
                'attributes',
            )
        }),
    ]

    def clean(self):
        # TODO clean class from attributes and attach to container
        pass


class Bootstrap4GridRowPlugin(CMSPluginBase):
    """
    Layout > Grid: "Row" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    model = Bootstrap4GridRow
    name = _('Grid - Row')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/plugins/grid_row.html'
    allow_children = True
    child_classes = ['Bootstrap4GridColumnPlugin']

    fieldsets = [
        (None, {
            'fields': (
                ('vertical_alignment', 'horizontal_alignment'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'gutters',
                'tag_type',
                'attributes',
            )
        }),
    ]


class Bootstrap4GridColumnPlugin(CMSPluginBase):
    """
    Layout > Grid: "Column" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    model = Bootstrap4GridColumn
    name = _('Grid - Column')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/plugins/grid_column.html'
    allow_children = True
    # require_parent = True
    # TODO it should allow for the responsive utilitiy class
    # https://getbootstrap.com/docs/4.0/layout/grid/#column-resets
    # parent_classes = ['Bootstrap4GridRowPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'column_type',
                ('column_size', 'column_alignment'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]
