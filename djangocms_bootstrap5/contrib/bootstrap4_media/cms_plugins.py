from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.helpers import concat_classes

from .models import Bootstrap5Media, Bootstrap5MediaBody


class Bootstrap5MediaPlugin(CMSPluginBase):
    """
    Layout > "Media" Plugin
    http://getbootstrap.com/docs/4.0/layout/media-object/
    """
    model = Bootstrap5Media
    name = _('Media')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/media.html'
    change_form_template = 'djangocms_bootstrap5/admin/media.html'
    allow_children = True

    fieldsets = [
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        classes = concat_classes([
            'media',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


class Bootstrap5MediaBodyPlugin(CMSPluginBase):
    """
    Layout > "Media body" Plugin
    http://getbootstrap.com/docs/4.0/layout/media-object/
    """
    model = Bootstrap5MediaBody
    name = _('Media body')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/media-body.html'
    change_form_template = 'djangocms_bootstrap5/admin/media.html'
    allow_children = True
    parent_classes = ['Bootstrap5MediaPlugin']

    fieldsets = [
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        classes = concat_classes([
            'media-body',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap5MediaPlugin)
plugin_pool.register_plugin(Bootstrap5MediaBodyPlugin)
