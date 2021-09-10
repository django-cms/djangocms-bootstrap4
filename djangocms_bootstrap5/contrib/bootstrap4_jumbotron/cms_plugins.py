from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.helpers import concat_classes

from .models import Bootstrap5Jumbotron


class Bootstrap5JumbotronPlugin(CMSPluginBase):
    """
    Components > "Jumbotron" Plugin
    https://getbootstrap.com/docs/5.0/components/jumbotron/
    """
    model = Bootstrap5Jumbotron
    name = _('Jumbotron')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/jumbotron.html'
    change_form_template = 'djangocms_bootstrap5/admin/jumbotron.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'fluid',
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
        link_classes = ['jumbotron']
        if instance.fluid:
            link_classes.append('jumbotron-fluid')

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap5JumbotronPlugin)
