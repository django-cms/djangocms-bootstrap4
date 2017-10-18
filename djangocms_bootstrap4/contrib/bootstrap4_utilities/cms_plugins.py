# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Spacing


class Bootstrap4SpacingPlugin(CMSPluginBase):
    """
    Components > "Card" Plugin
    https://getbootstrap.com/docs/4.0/components/card/
    """
    model = Bootstrap4Spacing
    name = _('Spacing')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/spacing.html'
    change_form_template = 'djangocms_bootstrap4/admin/spacing.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'space_property',
                'space_sides',
                'space_size',
                'space_device',
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
        spacing = '{}'.format(instance.space_property)
        if instance.space_sides:
            spacing += '{}'.format(instance.space_sides)
        if instance.space_device:
            spacing += '-{}'.format(instance.space_device)
        spacing += '-{}'.format(instance.space_size)

        classes = concat_classes([
            spacing,
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4SpacingPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4SpacingPlugin)
