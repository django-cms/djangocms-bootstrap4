from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.helpers import get_plugin_template

from .constants import TAB_TEMPLATE_CHOICES
from .models import Bootstrap5Tab, Bootstrap5TabItem


class Bootstrap5TabPlugin(CMSPluginBase):
    """
    Components > "Navs - Tab" Plugin
    https://getbootstrap.com/docs/5.0/components/navs/
    """
    model = Bootstrap5Tab
    name = _('Tabs')
    module = _('Bootstrap 5')
    change_form_template = 'djangocms_bootstrap5/admin/tabs.html'
    allow_children = True
    child_classes = ['Bootstrap5TabItemPlugin']

    fieldsets = [
        (None, {
            'fields': (
                ('tab_type', 'tab_alignment'),
                ('tab_index', 'tab_effect'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
                'tag_type',
                'attributes',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'tabs', 'tabs', TAB_TEMPLATE_CHOICES
        )


class Bootstrap5TabItemPlugin(CMSPluginBase):
    """
    Components > "Navs - Tab Item" Plugin
    https://getbootstrap.com/docs/5.0/components/navs/
    """
    model = Bootstrap5TabItem
    name = _('Tab item')
    module = _('Bootstrap 5')
    change_form_template = 'djangocms_bootstrap5/admin/tabs.html'
    allow_children = True
    parent_classes = ['Bootstrap5TabPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'tab_title',
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
        return get_plugin_template(
            instance.parent.get_plugin_instance()[0],
            'tabs',
            'item',
            TAB_TEMPLATE_CHOICES,
        )


plugin_pool.register_plugin(Bootstrap5TabPlugin)
plugin_pool.register_plugin(Bootstrap5TabItemPlugin)
