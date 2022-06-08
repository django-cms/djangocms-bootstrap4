from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.helpers import concat_classes

from .forms import Bootstrap5CodeForm
from .models import Bootstrap5Blockquote, Bootstrap5Code, Bootstrap5Figure


class Bootstrap5CodePlugin(CMSPluginBase):
    """
    Content > "Code" Plugin
    https://getbootstrap.com/docs/5.0/content/code/
    """
    model = Bootstrap5Code
    name = _('Code')
    module = _('Bootstrap 5')
    form = Bootstrap5CodeForm
    render_template = 'djangocms_bootstrap5/code.html'
    change_form_template = 'djangocms_bootstrap5/admin/code.html'
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


class Bootstrap5BlockquotePlugin(CMSPluginBase):
    """
    Content > "Blockquote" Plugin
    https://getbootstrap.com/docs/5.0/content/typography/#blockquotes
    """
    model = Bootstrap5Blockquote
    name = _('Blockquote')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/blockquote.html'
    change_form_template = 'djangocms_bootstrap5/admin/blockquote.html'
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

        return super().render(
            context, instance, placeholder
        )


class Bootstrap5FigurePlugin(CMSPluginBase):
    """
    Content > "Figure" Plugin
    https://getbootstrap.com/docs/5.0/content/figures/
    """
    model = Bootstrap5Figure
    name = _('Figure')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/figure.html'
    change_form_template = 'djangocms_bootstrap5/admin/figure.html'
    allow_children = True
    child_classes = ['Bootstrap5PicturePlugin']

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

        return super().render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap5CodePlugin)
plugin_pool.register_plugin(Bootstrap5BlockquotePlugin)
plugin_pool.register_plugin(Bootstrap5FigurePlugin)
