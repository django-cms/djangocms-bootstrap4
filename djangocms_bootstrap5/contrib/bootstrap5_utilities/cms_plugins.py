from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.helpers import concat_classes

from .models import Bootstrap5Spacing


class Bootstrap5SpacingPlugin(CMSPluginBase):
    """
    Components > "Card" Plugin
    https://getbootstrap.com/docs/5.0/components/card/
    """
    model = Bootstrap5Spacing
    name = _('Spacing')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/spacing.html'
    change_form_template = 'djangocms_bootstrap5/admin/spacing.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'space_property',
                'space_sides',
                'space_size',
                'space_device',
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
        instance.attributes['class'] = concat_classes([
            instance.get_base_css_class(),
            instance.attributes.get('class'),
        ])

        return super().render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap5SpacingPlugin)
