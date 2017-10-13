# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_link.cms_plugins import LinkPlugin
from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Link
from .forms import Bootstrap4LinkForm


class Bootstrap4LinkPlugin(LinkPlugin, CMSPluginBase):
    """
    Components > "Button" Plugin
    https://getbootstrap.com/docs/4.0/components/buttons/
    """
    model = Bootstrap4Link
    name = _('Link / Button')
    form = Bootstrap4LinkForm
    change_form_template = 'djangocms_bootstrap4/admin/link.html'
    module = _('Bootstrap 4')

    LinkPlugin.fieldsets[0] = (
        None, {
            'fields': (
                ('name', 'link_type'),
                ('external_link', 'internal_link'),
                ('link_context', 'link_size'),
                ('link_outline', 'link_block'),
            )
        }
    )

    fieldsets = LinkPlugin.fieldsets

    def render(self, context, instance, placeholder):
        linkClasses = []
        if instance.link_type == 'link':
            linkClasses.append('text-{}'.format(instance.link_context))
        else:
            linkClasses.append('btn')
            if not instance.link_outline:
                linkClasses.append(
                    'btn-{}'.format(instance.link_context)
                );
            else:
                linkClasses.append(
                    'btn-outline-{}'.format(instance.link_context)
                );
        if instance.link_size:
            linkClasses.append(instance.link_size);
        if instance.link_block:
            linkClasses.append('btn-block');

        classes = concat_classes(linkClasses + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4LinkPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.unregister_plugin(LinkPlugin)
plugin_pool.register_plugin(Bootstrap4LinkPlugin)
