# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import (
    Bootstrap4Collapse,
    Bootstrap4CollapseTrigger,
    Bootstrap4CollapseContainer,
)


class Bootstrap4CollapsePlugin(CMSPluginBase):
    """
    Component > "Collapse" Plugin
    https://getbootstrap.com/docs/4.0/components/collapse/
    """
    model = Bootstrap4Collapse
    name = _('Collapse')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/collapse.html'
    change_form_template = 'djangocms_bootstrap4/admin/collapse.html'
    allow_children = True
    child_classes = [
        'Bootstrap4CollapseTriggerPlugin',
        'Bootstrap4CollapseContainerPlugin',
        'Bootstrap4LinkPlugin',
        'Bootstrap4CardPlugin',
        'Bootstrap4SpacingPlugin',
        'Bootstrap4GridRowPlugin',
    ]

    fieldsets = [
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'siblings',
                'tag_type',
                'attributes',
            )
        }),
    ]


class Bootstrap4CollapseTriggerPlugin(CMSPluginBase):
    """
    Component > "Collapse" Plugin
    https://getbootstrap.com/docs/4.0/components/collapse/
    """
    model = Bootstrap4CollapseTrigger
    name = _('Collapse trigger')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/collapse-trigger.html'
    allow_children = True
    parent_classes = [
        'Bootstrap4CardPlugin',
        'Bootstrap4CardInnerPlugin',
        'Bootstrap4CollapsePlugin',
        'Bootstrap4GridColumnPlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                'identifier',
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


class Bootstrap4CollapseContainerPlugin(CMSPluginBase):
    """
    Component > "Collapse Container" Plugin
    https://getbootstrap.com/docs/4.0/components/collapse/
    """
    model = Bootstrap4CollapseContainer
    name = _('Collapse container')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/collapse-container.html'
    allow_children = True
    parent_classes = [
        'Bootstrap4CardPlugin',
        'Bootstrap4CardInnerPlugin',
        'Bootstrap4CollapsePlugin',
        'Bootstrap4GridColumnPlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                'identifier',
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
        classes = concat_classes([
            'collapse',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4CollapseContainerPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4CollapsePlugin)
plugin_pool.register_plugin(Bootstrap4CollapseTriggerPlugin)
plugin_pool.register_plugin(Bootstrap4CollapseContainerPlugin)
