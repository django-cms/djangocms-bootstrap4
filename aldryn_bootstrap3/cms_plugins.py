# -*- coding: utf-8 -*-
# from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

# from .models import BootstrapContainerPlugin

from .models import Boostrap3BlockquotePlugin, Boostrap3ButtonPlugin


# class Bootstrap3BlockquoteCMSPlugin(CMSPluginBase):
#     model = Boostrap3BlockquotePlugin
#     name = _("Blockquote")
#     render_template = 'aldryn_bootstrap3/plugins/blockquote.html'
#     allow_children = True
#
#     def render(self, context, instance, placeholder):
#         context.update({'instance': instance})
#         return context
#
# # plugin_pool.register_plugin(Bootstrap3BlockquoteCMSPlugin)


class Bootstrap3ButtonCMSPlugin(CMSPluginBase):
    model = Boostrap3ButtonPlugin
    name = _("Button")
    render_template = 'aldryn_bootstrap3/plugins/button.html'
    allow_children = True
    readonly_fields = (
        'preview',
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

    def preview(self, *args, **kwargs):
        from django.template.loader import render_to_string
        rendered = render_to_string('aldryn_bootstrap3/plugins/button_admin_preview.html', {})
        return rendered
    preview.allow_tags = True

plugin_pool.register_plugin(Bootstrap3ButtonCMSPlugin)


# Boostrap3AppdataPluginMultiform = app_data.multiform_factory(forms.Bootstrap3AppDataForm)


# class Bootstrap3AppdataCMSPlugin(app_data.admin.AppDataAdminMixin, CMSPluginBase):
#     model = Bootstrap3AppdataPlugin
#     name = _("My Appdata Plugin")
#     render_template = 'aldryn_bootstrap3/plugins/button.html'
#     allow_children = True
#     # multiform = Boostrap3AppdataPluginMultiform
#
#     declared_fieldsets = [
#         (None, {'fields': ['label', 'url',]}),
#         ('Bootstrap', {'fields': [('bootstrap3.breakpoints', 'bootstrap3.button_size', 'bootstrap3.button_types')]})
#     ]
#
#     def render(self, context, instance, placeholder):
#         context.update({'instance': instance})
#         return context
#
#     def get_form(self, request, obj=None, **kwargs):
#         """
#         Returns a Form class for use in the admin add view. This is used by
#         add_view and change_view.
#         """
#         if self.multiform is None:
#             return super(Bootstrap3AppdataCMSPlugin, self).get_form(request, obj=obj, **kwargs)
#         return app_data.forms.multiform_factory(self.model, **self._get_form_factory_opts(request, obj, **kwargs))
#
# plugin_pool.register_plugin(Bootstrap3AppdataCMSPlugin)


# class BootstrapContainerCMSPlugin(CMSPluginBase):
#     model = BootstrapContainerPlugin
#     name = _("Responsive Wrapper")
#     render_template = 'aldryn_responsive/plugins/wrapper.html'
#     allow_children = True
#
#     def render(self, context, instance, placeholder):
#         context.update({'instance': instance})
#         return context
#
# plugin_pool.register_plugin(ResponsiveWrapperCMSPlugin)
