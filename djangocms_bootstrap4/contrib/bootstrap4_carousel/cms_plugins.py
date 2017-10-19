# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_link.cms_plugins import LinkPlugin
from djangocms_bootstrap4.helpers import concat_classes, get_plugin_template

from .models import Bootstrap4Carousel, Bootstrap4CarouselSlide


class Bootstrap4CarouselPlugin(CMSPluginBase):
    """
    Components > "Carousel" Plugin
    https://getbootstrap.com/docs/4.0/components/carousel/
    """
    model = Bootstrap4Carousel
    name = _('Carousel')
    module = _('Bootstrap 4')
    allow_children = True
    child_classes = ['Bootstrap4CarouselSlidePlugin']

    fieldsets = [
        (None, {
            'fields': (
                ('carousel_style', 'carousel_interval'),
                ('carousel_controls', 'carousel_indicators'),
                ('carousel_keyboard', 'carousel_wrap'),
                ('carousel_ride', 'carousel_pause'),
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

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(instance, 'carousel', 'carousel')

    def render(self, context, instance, placeholder):
        link_classes = ['carousel', 'slide']

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4CarouselPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4CarouselSlidePlugin(CMSPluginBase):
    """
    Components > "Carousel Slide" Plugin
    https://getbootstrap.com/docs/4.0/components/carousel/
    """
    model = Bootstrap4CarouselSlide
    name = _('Carousel slide')
    module = _('Bootstrap 4')
    allow_children = True
    parent_classes = ['Bootstrap4CarouselPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'carousel_image',
                'carousel_content',
            )
        }),
        (_('Link settings'), {
            'classes': ('collapse',),
            'fields': (
                ('external_link', 'internal_link'),
                ('mailto', 'phone'),
                ('anchor', 'target'),
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
        context['instance'] = instance
        context['link'] = instance.get_link()
        return context

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(instance, 'carousel', 'slide')


plugin_pool.register_plugin(Bootstrap4CarouselPlugin)
plugin_pool.register_plugin(Bootstrap4CarouselSlidePlugin)
