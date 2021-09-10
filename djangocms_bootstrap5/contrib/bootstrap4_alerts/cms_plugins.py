from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.helpers import concat_classes

from .models import Bootstrap5Alerts


class Bootstrap5AlertsPlugin(CMSPluginBase):
    """
    Components > "Alerts" Plugin
    https://getbootstrap.com/docs/5.0/components/alerts/
    """
    model = Bootstrap5Alerts
    name = _('Alert')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/alerts.html'
    change_form_template = 'djangocms_bootstrap5/admin/alerts.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'alert_context',
                'alert_dismissable',
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
        link_classes = ['alert']
        link_classes.append('alert-{}'.format(instance.alert_context))

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap5AlertsPlugin)
