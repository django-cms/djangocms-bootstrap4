# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .blueprints import (
    create_card_blueprint,
    create_panel_blueprint,
    create_teaser_blueprint,
)
from .models import (
    Bootstrap4Card,
    Bootstrap4CardInner,
    Bootstrap4CardContent,
    Bootstrap4CardImage,
)
from .forms import Bootstrap4CardForm


class Bootstrap4CardPlugin(CMSPluginBase):
    """
    Components > "Card" Plugin
    https://getbootstrap.com/docs/4.0/components/card/
    """
    model = Bootstrap4Card
    name = _('Card')
    module = _('Bootstrap 4')
    form = Bootstrap4CardForm
    render_template = 'djangocms_bootstrap4/card.html'
    change_form_template = 'djangocms_bootstrap4/admin/card.html'
    allow_children = True
    child_classes = [
        'Bootstrap4CardPlugin',
        'Bootstrap4CardInnerPlugin',
        'Bootstrap4CardImagePlugin',
    ]
    # TODO also allow for ListGroup, Blockquote, Nav Tabs

    fieldsets = [
        (_('Blueprints'), {
            'classes': ('collapse',),
            'fields': (
                'blueprint',
            )
        }),
        (None, {
            'fields': (
                'card_type',
                ('card_context', 'card_alignment'),
                ('card_outline', 'card_text_color'),
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

    def save_model(self, request, obj, form, change):
        super(Bootstrap4CardPlugin, self).save_model(request, obj, form, change)
        data = form.cleaned_data

        if data['blueprint']:
            if data['blueprint'] == 'card':
                create_card_blueprint(obj)
            if data['blueprint'] == 'panel':
                create_panel_blueprint(obj)
            if data['blueprint'] == 'teaser':
                create_teaser_blueprint(obj)

    def render(self, context, instance, placeholder):
        linkClasses = []
        if instance.card_type:
            linkClasses.append(instance.card_type)
        if instance.card_context and instance.card_outline:
            linkClasses.append('border-{}'.format(instance.card_context))
        elif instance.card_context:
            linkClasses.append('bg-{}'.format(instance.card_context))
        if instance.card_alignment:
            linkClasses.append(instance.card_alignment)
        if instance.card_text_color:
            linkClasses.append('text-{}'.format(instance.card_text_color))

        classes = concat_classes(linkClasses + [
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
    allow_children = True
    parent_classes = ['Bootstrap4CardPlugin']

    fieldsets = [
        (None, {
            'fields': (
                ('inner_type', 'tag_type'),
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        linkClasses = []
        if instance.inner_type:
            linkClasses.append(instance.inner_type)

        classes = concat_classes(linkClasses + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4CardInnerPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4CardContentPlugin(CMSPluginBase):
    """
    Components > "Card - Content" Plugin (Title, Subtitle, Text, Link)
    https://getbootstrap.com/docs/4.0/components/card/
    """
    model = Bootstrap4CardContent
    name = _('Card content')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/card_content.html'
    allow_children = True
    parent_classes = [
        'Bootstrap4CardInnerPlugin',
        'Bootstrap4CardImagePlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                ('content_type', 'tag_type'),
                'card_content',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        linkClasses = []
        if instance.content_type:
            linkClasses.append(instance.content_type)

        classes = concat_classes(linkClasses + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4CardContentPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4CardImagePlugin(CMSPluginBase):
    """
    Components > "Card - Image" Plugin (Top, Bottom, Overlay)
    https://getbootstrap.com/docs/4.0/components/card/
    """
    model = Bootstrap4CardImage
    name = _('Card image')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/card.html'
    allow_children = True
    parent_classes = [
        'Bootstrap4CardPlugin',
        'Bootstrap4CardInnerPlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                ('content_type', 'tag_type'),
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        linkClasses = []
        if instance.content_type:
            linkClasses.append(instance.content_type)
        else:
            linkClasses.append('card-img')

        classes = concat_classes(linkClasses + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4CardImagePlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4CardPlugin)
plugin_pool.register_plugin(Bootstrap4CardInnerPlugin)
plugin_pool.register_plugin(Bootstrap4CardContentPlugin)
plugin_pool.register_plugin(Bootstrap4CardImagePlugin)
