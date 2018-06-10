# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool

from djangocms_link.cms_plugins import LinkPlugin
from djangocms_link.models import get_templates
from djangocms_bootstrap4.helpers import concat_classes, get_plugin_template

from .constants import USE_LINK_ICONS
from .models import Bootstrap4Link
from .forms import Bootstrap4LinkForm


class Bootstrap4LinkPlugin(LinkPlugin):
    """
    Components > "Button" Plugin
    https://getbootstrap.com/docs/4.0/components/buttons/
    """
    model = Bootstrap4Link
    name = _('Link / Button')
    form = Bootstrap4LinkForm
    change_form_template = 'djangocms_bootstrap4/admin/link.html'
    module = _('Bootstrap 4')

    fields = (
        ('name', 'link_type'),
        ('external_link', 'internal_link'),
        ('link_context', 'link_size'),
        ('link_outline', 'link_block'),
    )

    if USE_LINK_ICONS:
        fields = fields + (
            ('icon_left', 'icon_right'),
        )

    LinkPlugin.fieldsets[0] = (
        None, {
            'fields': fields
        }
    )

    fieldsets = LinkPlugin.fieldsets

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'link', 'link', get_templates()
        )

    def render(self, context, instance, placeholder):
        link_classes = []
        if instance.link_context:
            if instance.link_type == 'link':
                link_classes.append('text-{}'.format(instance.link_context))
            else:
                link_classes.append('btn')
                if not instance.link_outline:
                    link_classes.append(
                        'btn-{}'.format(instance.link_context)
                    )
                else:
                    link_classes.append(
                        'btn-outline-{}'.format(instance.link_context)
                    )
        if instance.link_size:
            link_classes.append(instance.link_size)
        if instance.link_block:
            link_classes.append('btn-block')

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4LinkPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.unregister_plugin(LinkPlugin)
plugin_pool.register_plugin(Bootstrap4LinkPlugin)
