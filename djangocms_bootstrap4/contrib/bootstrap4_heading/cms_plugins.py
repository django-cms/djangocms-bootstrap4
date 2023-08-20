from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.db import models
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _

from djangocms_bootstrap4.contrib.bootstrap4_heading.models import Bootstrap4Heading


@plugin_pool.register_plugin
class Bootstrap4HeadingPlugin(CMSPluginBase):
    model = Bootstrap4Heading
    name = _('Heading')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/heading.html'
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'name',
                'tag',
                'alignment',
                'color',
                'type',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'size',
                'size_unit',
                'attributes',
            )
        }),
    ]

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 2})
        },
    }
