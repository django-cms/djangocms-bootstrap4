# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from functools import partial

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext

from cms.models.pluginmodel import CMSPlugin
import cms.models
import cms.models.fields

import filer.fields.file

from . import model_fields, constants
from .conf import settings


##########
# Mixins #  do NOT use outside of this package!
##########  Because changes here might require Database migrations!


class LinkMixin(models.Model):
    url = models.URLField(_("link"), blank=True, default='')
    page_link = cms.models.fields.PageField(
        verbose_name=_("page"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    file = filer.fields.file.FilerFileField(
        verbose_name=_("file"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    anchor = models.CharField(
        _("anchor"), max_length=128, blank=True,
        help_text=_("Adds this value as an anchor (#my-anchor) to the link."),
    )
    mailto = models.EmailField(
        _("mailto"), blank=True, null=True,
        # help_text=_("An email address has priority over a text link."),
    )
    phone = models.CharField(
        _('Phone'), blank=True, null=True, max_length=40,
        # help_text=_('A phone number has priority over a mailto link.'),
    )
    target = models.CharField(
        _("target"), blank=True, max_length=100,
        choices=((
            ("", _("same window")),
            ("_blank", _("new window")),
            ("_parent", _("parent window")),
            ("_top", _("topmost frame")),
        ))
    )

    class Meta:
        abstract = True

    def get_url(self):
        if self.phone:
            link = u"tel://{}".format(self.phone)
        elif self.mailto:
            link = u"mailto:{}".format(self.mailto)
        elif self.url:
            link = self.url
        elif self.page_link_id:
            link = self.page_link.get_absolute_url()
        elif self.file:
            link = self.file.url
        else:
            link = ""
        if self.anchor:
            link += '#{}'.format(self.anchor)
        return link


#################
# Basic Plugins #
#################

@python_2_unicode_compatible
class Boostrap3ButtonPlugin(CMSPlugin, LinkMixin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    context = model_fields.Context(
        choices=constants.BUTTON_CONTEXT_CHOICES,
        default=constants.BUTTON_CONTEXT_DEFAULT,
    )
    size = model_fields.Size()

    icon_left = model_fields.Icon()
    icon_right = model_fields.Icon()

    classes = model_fields.Classes()

    label = models.CharField(_("label"), max_length=256, blank=True, default='')

    def __str__(self):
        return self.label


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

ColSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default='',
    min_value=1,
    max_value=constants.GRID_SIZE
)

OffsetSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default='',
    min_value=1,
    max_value=constants.GRID_SIZE
)

PushSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default='',
    min_value=1,
    max_value=constants.GRID_SIZE
)

PullSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default='',
    min_value=1,
    max_value=constants.GRID_SIZE
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
    tag = models.SlugField(default='div')

    def __str__(self):
        txt = ' '.join([self.get_column_classes(), self.classes])
        if self.tag != 'div':
            txt = '{} ({})'.format(txt, self.tag)
        return txt

    def get_class(self, device, element):
        size = getattr(self, '{}_{}'.format(device, element))
        if size:
            return '{}-{}-{}'.format(element, device, size)
        return ''

    def get_column_classes(self):
        classes = []
        for device in self.DEVICE_SIZES:
            for element in ('col', 'offset', 'push', 'pull'):
                classes.append(self.get_class(device, element))
        return ' '.join(cls for cls in classes if cls)

for size, name in constants.DEVICE_CHOICES:
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_col'.format(size),
        ColSizeField(verbose_name=_('col-{}-'.format(size))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_offset'.format(size),
        OffsetSizeField(verbose_name=_('col-{}-offset-'.format(size))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_push'.format(size),
        PushSizeField(verbose_name=_('col-{}-push-'.format(size))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_pull'.format(size),
        PullSizeField(verbose_name=_('col-{}-pull-'.format(size))),
    )

