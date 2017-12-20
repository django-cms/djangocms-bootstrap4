# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Navs, Bootstrap4NavItem


class Bootstrap4NavPlugin(CMSPluginBase):
    """
    Components > "Navs" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    model = Bootstrap4Navs
    name = _('Navs')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/navs.html'
    change_form_template = 'djangocms_bootstrap4/admin/navs.html'
    allow_children = True
    child_classes = [
        'Bootstrap4NavItemPlugin',
        'Bootstrap4GridRowPlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                'nav_style',
                'nav_alignment',
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

    def render(self, context, instance, placeholder):
        linkClasses = ['nav']
        if instance.nav_style:
            linkClasses.append(instance.nav_style)
        if instance.nav_alignment:
            linkClasses.append(instance.nav_alignment)

        classes = concat_classes(linkClasses + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4NavPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4NavItemPlugin(CMSPluginBase):
    """
    Components > "Nav Item" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    model = Bootstrap4NavItem
    name = _('Nav item')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/navs.html'
    change_form_template = 'djangocms_bootstrap4/admin/navs.html'
    allow_children = True
    parent_classes = [
        'Bootstrap4NavPlugin',
        'Bootstrap4GridColumnPlugin',
    ]

    fieldsets = [
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        classes = concat_classes([
            'nav-item',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4NavItemPlugin, self).render(
            context, instance, placeholder
        )

plugin_pool.register_plugin(Bootstrap4NavPlugin)
plugin_pool.register_plugin(Bootstrap4NavItemPlugin)
