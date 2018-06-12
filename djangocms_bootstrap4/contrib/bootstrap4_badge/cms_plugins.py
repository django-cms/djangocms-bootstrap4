# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Badge


class Bootstrap4BadgePlugin(CMSPluginBase):
    """
    Components > "Badge" Plugin
    https://getbootstrap.com/docs/4.0/components/badge/
    """
    model = Bootstrap4Badge
    name = _('Badge')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/badge.html'
    change_form_template = 'djangocms_bootstrap4/admin/badge.html'
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'badge_text',
                'badge_context',
                'badge_pills',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        link_classes = ['badge']
        if instance.badge_pills:
            link_classes.append('badge-pill')
        link_classes.append('badge-{}'.format(instance.badge_context))

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4BadgePlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4BadgePlugin)
