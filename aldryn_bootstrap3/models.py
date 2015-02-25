# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from functools import partial

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext

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


########
# Grid #
########

ColumnSizeField = partial(
    models.IntegerField,
    null=True,
    blank=True,
    default=1,
)

OffsetSizeField = partial(
    models.IntegerField,
    null=True,
    blank=True,
    default=0,
)


@python_2_unicode_compatible
class Bootstrap3RowPlugin(CMSPlugin):
    classes = model_fields.Classes()

    def __str__(self):
        column_count = self.cmsplugin_set.all().count()
        column_count_str = ungettext(
            "1 column",
            "%(count)i columns",
            column_count
        ) % (
            {'count': column_count}
        )
        if self.classes:
            return "{} ({})".format(
                self.classes,
                column_count_str
            )
        else:
            return column_count_str


@python_2_unicode_compatible
class Bootstrap3ColumnPlugin(CMSPlugin):
    DEVICE_CHOICES = constants.DEVICE_CHOICES
    DEVICE_SIZES = constants.DEVICE_SIZES

    classes = model_fields.Classes()

    def __str__(self):
        return ' '.join([self.get_column_classes(), self.classes])

    def get_column_size_class(self, size):
        # get column_size (a number) configured for this device_size
        column_size = getattr(self, '{}_size'.format(size))
        if column_size:
            return 'col-{}-{}'.format(size, column_size)
        return ''

    def get_column_offset_class(self, size):
        # get column_size (a number) configured for this device_size
        column_size = getattr(self, '{}_offset'.format(size))
        if column_size:
            return 'col-{}-{}-offset'.format(size, column_size)
        return ''

    def get_column_classes(self):
        size_classes = [
            self.get_column_size_class(size)
            for size in self.DEVICE_SIZES
        ]
        offset_classes = [
            self.get_column_offset_class(size)
            for size in self.DEVICE_SIZES
        ]
        classes = size_classes + offset_classes
        return ' '.join(html_class for html_class in classes if html_class)

for size, name in constants.DEVICE_CHOICES:
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_size'.format(size),
        ColumnSizeField(verbose_name=_('{} size'.format(name))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_offset'.format(size),
        OffsetSizeField(verbose_name=_('{} offset'.format(name))),
    )

