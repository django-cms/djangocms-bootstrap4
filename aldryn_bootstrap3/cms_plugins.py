# -*- coding: utf-8 -*-
# from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

# from .models import BootstrapContainerPlugin

from .models import Boostrap3BlockquotePlugin, Boostrap3ButtonPlugin


class Bootstrap3BlockquoteCMSPlugin(CMSPluginBase):
    model = Boostrap3BlockquotePlugin
    name = _("Blockquote")
    render_template = 'aldryn_bootstrap3/plugins/blockquote.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

# plugin_pool.register_plugin(Bootstrap3BlockquoteCMSPlugin)


class Bootstrap3ButtonCMSPlugin(CMSPluginBase):
    model = Boostrap3ButtonPlugin
    name = _("Button")
    render_template = 'aldryn_bootstrap3/plugins/button.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3ButtonCMSPlugin)



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
