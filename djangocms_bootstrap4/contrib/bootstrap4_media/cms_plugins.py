# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Media, Bootstrap4MediaBody


class Bootstrap4MediaPlugin(CMSPluginBase):
    """
    Layout > "Media" Plugin
    http://getbootstrap.com/docs/4.0/layout/media-object/
    """
    model = Bootstrap4Media
    name = _('Media')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/media.html'
    change_form_template = 'djangocms_bootstrap4/admin/media.html'
    allow_children = True

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
            'media',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4MediaPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4MediaBodyPlugin(CMSPluginBase):
    """
    Layout > "Media body" Plugin
    http://getbootstrap.com/docs/4.0/layout/media-object/
    """
    model = Bootstrap4MediaBody
    name = _('Media body')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/media-body.html'
    change_form_template = 'djangocms_bootstrap4/admin/media.html'
    allow_children = True
    parent_classes = ['Bootstrap4MediaPlugin']

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
            'media-body',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4MediaBodyPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4MediaPlugin)
plugin_pool.register_plugin(Bootstrap4MediaBodyPlugin)
