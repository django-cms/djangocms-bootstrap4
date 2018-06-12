# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Jumbotron


class Bootstrap4JumbotronPlugin(CMSPluginBase):
    """
    Components > "Jumbotron" Plugin
    https://getbootstrap.com/docs/4.0/components/jumbotron/
    """
    model = Bootstrap4Jumbotron
    name = _('Jumbotron')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/jumbotron.html'
    change_form_template = 'djangocms_bootstrap4/admin/jumbotron.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'fluid',
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
        link_classes = ['jumbotron']
        if instance.fluid:
            link_classes.append('jumbotron-fluid')

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4JumbotronPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4JumbotronPlugin)
