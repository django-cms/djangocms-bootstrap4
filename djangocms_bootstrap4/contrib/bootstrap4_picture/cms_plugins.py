# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import copy

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool

from djangocms_picture.cms_plugins import PicturePlugin
from djangocms_bootstrap4.helpers import concat_classes

from .models import Bootstrap4Picture


class Bootstrap4PicturePlugin(PicturePlugin):
    """
    Content > "Image" Plugin
    https://getbootstrap.com/docs/4.0/content/images/
    """
    model = Bootstrap4Picture
    name = _('Picture / Image')
    change_form_template = 'djangocms_bootstrap4/admin/picture.html'
    module = _('Bootstrap 4')

    fieldsets = copy.deepcopy(PicturePlugin.fieldsets)
    fieldsets[0] = (
        None, {
            'fields': (
                'picture',
                'external_picture',
                ('picture_fluid', 'picture_rounded', 'picture_thumbnail'),
            )
        }
    )

    def render(self, context, instance, placeholder):
        link_classes = []
        if instance.picture_fluid:
            link_classes.append('img-fluid')
        if instance.picture_rounded:
            link_classes.append('rounded')
        if instance.picture_thumbnail:
            link_classes.append('img-thumbnail')

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4PicturePlugin, self).render(
            context, instance, placeholder
        )


plugin_pool.unregister_plugin(PicturePlugin)
plugin_pool.register_plugin(Bootstrap4PicturePlugin)
