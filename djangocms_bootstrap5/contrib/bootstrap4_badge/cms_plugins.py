from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.helpers import concat_classes

from .models import Bootstrap5Badge


class Bootstrap5BadgePlugin(CMSPluginBase):
    """
    Components > "Badge" Plugin
    https://getbootstrap.com/docs/5.0/components/badge/
    """
    model = Bootstrap5Badge
    name = _('Badge')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/badge.html'
    change_form_template = 'djangocms_bootstrap5/admin/badge.html'
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'badge_text',
                'badge_context',
                'badge_pills',
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
        link_classes = ['badge']
        if instance.badge_pills:
            link_classes.append('badge-pill')
        link_classes.append('badge-{}'.format(instance.badge_context))

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap5BadgePlugin)
