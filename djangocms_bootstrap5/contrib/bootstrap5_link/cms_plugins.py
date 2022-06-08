import copy

from django.utils.translation import gettext_lazy as _

from cms.plugin_pool import plugin_pool

from djangocms_link.cms_plugins import LinkPlugin
from djangocms_link.models import get_templates

from djangocms_bootstrap5.helpers import concat_classes, get_plugin_template

from .constants import USE_LINK_ICONS
from .forms import Bootstrap5LinkForm
from .models import Bootstrap5Link


class Bootstrap5LinkPlugin(LinkPlugin):
    """
    Components > "Button" Plugin
    https://getbootstrap.com/docs/5.0/components/buttons/
    """
    model = Bootstrap5Link
    name = _('Link / Button')
    form = Bootstrap5LinkForm
    change_form_template = 'djangocms_bootstrap5/admin/link.html'
    module = _('Bootstrap 5')

    fields = (
        ('name', 'link_type'),
        ('external_link', 'internal_link'),
        ('link_context', 'link_size'),
        ('link_outline', 'link_block'),
    )

    if USE_LINK_ICONS:  # pragma: no cover
        fields = fields + (
            ('icon_left', 'icon_right'),
        )

    fieldsets = copy.deepcopy(LinkPlugin.fieldsets)
    fieldsets[0] = (
        None, {
            'fields': fields
        }
    )

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'link', 'link', get_templates()
        )

    def render(self, context, instance, placeholder):
        link_classes = []
        if instance.link_context:
            if instance.link_type == 'link':
                link_classes.append(f'text-{instance.link_context}')
            else:
                link_classes.append('btn')
                if not instance.link_outline:
                    link_classes.append(
                        f'btn-{instance.link_context}'
                    )
                else:
                    link_classes.append(
                        f'btn-outline-{instance.link_context}'
                    )
        if instance.link_size:
            link_classes.append(instance.link_size)
        if instance.link_block:
            link_classes.append('btn-block')

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


plugin_pool.unregister_plugin(LinkPlugin)
plugin_pool.register_plugin(Bootstrap5LinkPlugin)
