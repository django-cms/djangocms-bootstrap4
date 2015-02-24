# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from . import model_fields

from .conf import settings


@python_2_unicode_compatible
class Boostrap3BlockquotePlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)  # I saw this in aldryn-style

    breakpoints = models.CharField(max_length=255, blank=True, default='')
    context = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return 'Blockquote: '

    def get_css_classes(self):
        return ['an-example-class']


@python_2_unicode_compatible
class Boostrap3ButtonPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)  # I saw this in aldryn-style

    # breakpoints = models.CharField(max_length=255, blank=True, default='')
    breakpoints = model_fields.Breakpoint()
    context = models.CharField(max_length=255, blank=True, default='')

    label = models.CharField(_("label"), max_length=256, blank=True, default='')
    url = models.URLField(_("link"), blank=True, default='')

    def __str__(self):
        return self.label


# @python_2_unicode_compatible
# class Boostrap3ContainerPlugin(CMSPlugin):
#     breakpoints = models.CharField()
#     # context = ...  default/muted/primary/success
#
#     def __str__(self):
#         return u'Desktop: %s, Tablets: %s, Phones: %s' % (self.desktop, self.tablet, self.phone)
#
#     def get_class(self):
#         classes = {
#             # Phone, Tablet, Desktop: class
#             '100': 'visible-phone',
#             '010': 'visible-tablet',
#             '001': 'visible-desktop',
#             '011': 'hidden-phone',
#             '101': 'hidden-tablet',
#             '110': 'hidden-desktop',
#             '000': '',
#             '111': '',
#         }
#
#         return classes['%i%i%i' % (self.phone, self.tablet, self.desktop)]
