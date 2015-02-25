# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from . import model_fields, constants
from .conf import settings


#################
# Basic Plugins #
#################

@python_2_unicode_compatible
class Boostrap3ButtonPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    context = model_fields.Context(
        choices=constants.BUTTON_CONTEXT_CHOICES,
        default=constants.BUTTON_CONTEXT_DEFAULT,
    )
    size = model_fields.Size()
    classes = model_fields.Classes()

    label = models.CharField(_("label"), max_length=256, blank=True, default='')
    url = models.URLField(_("link"), blank=True, default='')

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Boostrap3BlockquotePlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    reverse = models.BooleanField(default=False, blank=True)
    classes = model_fields.Classes()

    def __str__(self):
        return 'Blockquote: '


@python_2_unicode_compatible
class Boostrap3BlockquotePlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    reverse = models.BooleanField(default=False, blank=True)
    classes = model_fields.Classes()

    def __str__(self):
        return 'Blockquote: '


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
