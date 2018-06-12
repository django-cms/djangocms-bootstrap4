# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4ListGroup, Bootstrap4ListGroupItem


class Bootstrap4ListGroupPlugin(CMSPluginBase):
    """
    Components > "List Group" Plugin
    https://getbootstrap.com/docs/4.0/components/list-group/
    """
    model = Bootstrap4ListGroup
    name = _('List group')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/list-group.html'
    change_form_template = 'djangocms_bootstrap4/admin/list-group.html'
    allow_children = True
    child_classes = ['Bootstrap4ListGroupItemPlugin', 'Bootstrap4LinkPlugin']
    # TODO consider linking to tab-content

    fieldsets = [
        (None, {
            'fields': (
                'list_group_flush',
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
        link_classes = ['list-group']
        if instance.list_group_flush:
            link_classes.append('list-group-flush')

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4ListGroupPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4ListGroupItemPlugin(CMSPluginBase):
    """
    Components > "List Group Item" Plugin
    https://getbootstrap.com/docs/4.0/components/list-group/
    """
    model = Bootstrap4ListGroupItem
    name = _('List item')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/list-group-item.html'
    change_form_template = 'djangocms_bootstrap4/admin/list-group.html'
    allow_children = True
    parent_classes = ['Bootstrap4ListGroupPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'list_context',
                'list_state',
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
        link_classes = ['list-group-item']
        if instance.list_context:
            link_classes.append('list-group-item-{}'.format(instance.list_context))
        if instance.list_state:
            link_classes.append(instance.list_state)

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4ListGroupItemPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4ListGroupPlugin)
plugin_pool.register_plugin(Bootstrap4ListGroupItemPlugin)
