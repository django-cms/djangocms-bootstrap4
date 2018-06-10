# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.helpers import concat_classes

from .forms import Bootstrap4CodeForm
from .models import Bootstrap4Code, Bootstrap4Blockquote, Bootstrap4Figure


class Bootstrap4CodePlugin(CMSPluginBase):
    """
    Content > "Code" Plugin
    https://getbootstrap.com/docs/4.0/content/code/
    """
    model = Bootstrap4Code
    name = _('Code')
    module = _('Bootstrap 4')
    form = Bootstrap4CodeForm
    render_template = 'djangocms_bootstrap4/code.html'
    change_form_template = 'djangocms_bootstrap4/admin/code.html'
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'code_content',
                'tag_type',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]


class Bootstrap4BlockquotePlugin(CMSPluginBase):
    """
    Content > "Blockquote" Plugin
    https://getbootstrap.com/docs/4.0/content/typography/#blockquotes
    """
    model = Bootstrap4Blockquote
    name = _('Blockquote')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/blockquote.html'
    change_form_template = 'djangocms_bootstrap4/admin/blockquote.html'
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                ('quote_content', 'quote_origin'),
                'quote_alignment',
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
        link_classes = ['blockquote']
        if instance.quote_alignment:
            link_classes.append(instance.quote_alignment)
        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4BlockquotePlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4FigurePlugin(CMSPluginBase):
    """
    Content > "Figure" Plugin
    https://getbootstrap.com/docs/4.0/content/figures/
    """
    model = Bootstrap4Figure
    name = _('Figure')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/figure.html'
    change_form_template = 'djangocms_bootstrap4/admin/figure.html'
    allow_children = True
    child_classes = ['Bootstrap4PicturePlugin']

    fieldsets = [
        (None, {
            'fields': (
                'figure_caption',
                'figure_alignment',
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
        classes = concat_classes([
            'figure',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4FigurePlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap4CodePlugin)
plugin_pool.register_plugin(Bootstrap4BlockquotePlugin)
plugin_pool.register_plugin(Bootstrap4FigurePlugin)
