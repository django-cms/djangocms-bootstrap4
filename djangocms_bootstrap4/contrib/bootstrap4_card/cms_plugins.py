# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Card, Bootstrap4CardInner


class Bootstrap4CardPlugin(CMSPluginBase):
    """
    Components > "Card" Plugin
    https://getbootstrap.com/docs/4.0/components/card/
    """
    model = Bootstrap4Card
    name = _('Card')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/card.html'
    change_form_template = 'djangocms_bootstrap4/admin/card.html'
    allow_children = True
    child_classes = [
        'Bootstrap4CardPlugin',
        'Bootstrap4CardInnerPlugin',
        'Bootstrap4LinkPlugin',
        'Bootstrap4ListGroupPlugin',
        'Bootstrap4PicturePlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                'card_type',
                ('card_context', 'card_text_color'),
                ('card_alignment', 'card_outline'),
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
        link_classes = []
        if instance.card_type:
            link_classes.append(instance.card_type)
        if instance.card_context and instance.card_outline:
            link_classes.append('border-{}'.format(instance.card_context))
        elif instance.card_context:
            link_classes.append('bg-{}'.format(instance.card_context))
        if instance.card_alignment:
            link_classes.append(instance.card_alignment)
        if instance.card_text_color:
            link_classes.append('text-{}'.format(instance.card_text_color))

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4CardPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4CardInnerPlugin(CMSPluginBase):
    """
    Components > "Card - Inner" Plugin (Header, Footer, Body)
    https://getbootstrap.com/docs/4.0/components/card/
    """
    model = Bootstrap4CardInner
    name = _('Card inner')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/card.html'
    change_form_template = 'djangocms_bootstrap4/admin/card.html'
    allow_children = True
    parent_classes = [
        'Bootstrap4CardPlugin',
        'Bootstrap4CollapseTriggerPlugin',
        'Bootstrap4CollapseContainerPlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                'inner_type',
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
        link_classes = []
        if instance.inner_type:
            link_classes.append(instance.inner_type)

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4CardInnerPlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4CardPlugin)
plugin_pool.register_plugin(Bootstrap4CardInnerPlugin)
