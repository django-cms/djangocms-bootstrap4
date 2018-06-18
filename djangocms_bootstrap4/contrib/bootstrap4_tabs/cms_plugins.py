# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import get_plugin_template

from .constants import TAB_TEMPLATE_CHOICES
from .models import Bootstrap4Tab, Bootstrap4TabItem


class Bootstrap4TabPlugin(CMSPluginBase):
    """
    Components > "Navs - Tab" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    model = Bootstrap4Tab
    name = _('Tabs')
    module = _('Bootstrap 4')
    change_form_template = 'djangocms_bootstrap4/admin/tabs.html'
    allow_children = True
    child_classes = ['Bootstrap4TabItemPlugin']

    fieldsets = [
        (None, {
            'fields': (
                ('tab_type', 'tab_alignment'),
                ('tab_index', 'tab_effect'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
                'tag_type',
                'attributes',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'tabs', 'tabs', TAB_TEMPLATE_CHOICES
        )


class Bootstrap4TabItemPlugin(CMSPluginBase):
    """
    Components > "Navs - Tab Item" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    model = Bootstrap4TabItem
    name = _('Tab item')
    module = _('Bootstrap 4')
    change_form_template = 'djangocms_bootstrap4/admin/tabs.html'
    allow_children = True
    parent_classes = ['Bootstrap4TabPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'tab_title',
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

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance.parent.get_plugin_instance()[0],
            'tabs',
            'item',
            TAB_TEMPLATE_CHOICES,
        )


plugin_pool.register_plugin(Bootstrap4TabPlugin)
plugin_pool.register_plugin(Bootstrap4TabItemPlugin)
