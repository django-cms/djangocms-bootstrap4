# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_picture.cms_plugins import PicturePlugin
from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Picture


class Bootstrap4PicturePlugin(PicturePlugin, CMSPluginBase):
    """
    Content > "Image" Plugin
    https://getbootstrap.com/docs/4.0/content/images/
    """
    model = Bootstrap4Picture
    name = _('Image')
    change_form_template = 'djangocms_bootstrap4/admin/picture.html'
    module = _('Bootstrap 4')

    PicturePlugin.fieldsets[0] = (
        None, {
            'fields': (
                'picture',
                'external_picture',
                ('picture_fluid', 'picture_rounded', 'picture_thumbnail'),
            )
        }
    )

    fieldsets = PicturePlugin.fieldsets

    def render(self, context, instance, placeholder):
        linkClasses = []
        if instance.picture_fluid:
            linkClasses.append('img-fluid')
        if instance.picture_rounded:
            linkClasses.append('rounded')
        if instance.picture_thumbnail:
            linkClasses.append('img-thumbnail')

        classes = concat_classes(linkClasses + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4PicturePlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.unregister_plugin(PicturePlugin)
plugin_pool.register_plugin(Bootstrap4PicturePlugin)
