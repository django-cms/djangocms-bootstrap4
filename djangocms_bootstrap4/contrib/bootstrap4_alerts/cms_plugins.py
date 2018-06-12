# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Alerts


class Bootstrap4AlertsPlugin(CMSPluginBase):
    """
    Components > "Alerts" Plugin
    https://getbootstrap.com/docs/4.0/components/alerts/
    """
    model = Bootstrap4Alerts
    name = _('Alert')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/alerts.html'
    change_form_template = 'djangocms_bootstrap4/admin/alerts.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'alert_context',
                'alert_dismissable',
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
        link_classes = ['alert']
        link_classes.append('alert-{}'.format(instance.alert_context))

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4AlertsPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4AlertsPlugin)
