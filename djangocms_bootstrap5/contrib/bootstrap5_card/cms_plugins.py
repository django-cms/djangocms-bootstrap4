from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.helpers import concat_classes

from .models import Bootstrap5Card, Bootstrap5CardInner


class Bootstrap5CardPlugin(CMSPluginBase):
    """
    Components > "Card" Plugin
    https://getbootstrap.com/docs/5.0/components/card/
    """
    model = Bootstrap5Card
    name = _('Card')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/card.html'
    change_form_template = 'djangocms_bootstrap5/admin/card.html'
    allow_children = True
    child_classes = [
        'Bootstrap5CardPlugin',
        'Bootstrap5CardInnerPlugin',
        'Bootstrap5LinkPlugin',
        'Bootstrap5ListGroupPlugin',
        'Bootstrap5PicturePlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                'card_type',
                ('card_context', 'card_text_color'),
                ('card_alignment', 'card_outline'),
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
        link_classes = [instance.card_type]
        if instance.card_context and instance.card_outline:
            link_classes.append('border-{}'.format(instance.card_context))
        elif instance.card_context:
            link_classes.append('bg-{}'.format(instance.card_context))
        if instance.card_alignment:
            link_classes.append(instance.card_alignment)
        if instance.card_text_color:
            link_classes.append('text-{}'.format(instance.card_text_color))

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


class Bootstrap5CardInnerPlugin(CMSPluginBase):
    """
    Components > "Card - Inner" Plugin (Header, Footer, Body)
    https://getbootstrap.com/docs/5.0/components/card/
    """
    model = Bootstrap5CardInner
    name = _('Card inner')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/card.html'
    change_form_template = 'djangocms_bootstrap5/admin/card.html'
    allow_children = True
    parent_classes = [
        'Bootstrap5CardPlugin',
        'Bootstrap5CollapseTriggerPlugin',
        'Bootstrap5CollapseContainerPlugin',
    ]

    fieldsets = [
        (None, {
            'fields': (
                'inner_type',
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
        classes = concat_classes([instance.inner_type] + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap5CardPlugin)
plugin_pool.register_plugin(Bootstrap5CardInnerPlugin)
