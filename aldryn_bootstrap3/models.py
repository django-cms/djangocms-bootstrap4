# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from functools import partial

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext

from cms.models.pluginmodel import CMSPlugin
import cms.models

from . import model_fields, constants
from .conf import settings


##########
# Mixins #  do NOT use outside of this package!
##########  Because changes here might require Database migrations!


class LinkMixin(models.Model):
    url = models.URLField(_("link"), blank=True, default='')
    page_link = models.ForeignKey(
        cms.models.Page,
        verbose_name=_("page"),
        blank=True,
        null=True,
        # help_text=_("A link to a page has priority over a text link."),
        on_delete=models.SET_NULL
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
        print "I AM THE LINK"
        if self.phone:
            link = u"tel://{}".format(self.phone)
        elif self.mailto:
            link = u"mailto:{}".format(self.mailto)
        elif self.url:
            link = self.url
        elif self.page_link_id:
            link = self.page_link.get_absolute_url()
        else:
            link = ""
        if self.anchor:
            link += '#{}'.format(self.anchor)
        print "LINK: ", link
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

PushSizeField = partial(
    models.IntegerField,
    null=True,
    blank=True,
    default=0,
)

PullSizeField = partial(
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

    def get_col_class(self, device):
        col = getattr(self, '{}_col'.format(device))
        if col:
            return 'col-{}-{}'.format(device, col)
        return ''

    def get_offset_class(self, device):
        offset = getattr(self, '{}_offset'.format(device))
        if offset:
            return 'offset-{}-{}'.format(device, offset)
        return ''

    def get_push_class(self, device):
        push = getattr(self, '{}_offset'.format(device))
        if push:
            return 'push-{}-{}'.format(device, push)
        return ''

    def get_pull_class(self, device):
        pull = getattr(self, '{}_offset'.format(device))
        if pull:
            return 'pull-{}-{}'.format(device, pull)
        return ''

    def get_column_classes(self):
        size_classes = [
            self.get_col_class(device)
            for device in self.DEVICE_SIZES
        ]
        offset_classes = [
            self.get_offset_class(device)
            for device in self.DEVICE_SIZES
        ]
        push_classes = [
            self.get_push_class(device)
            for device in self.DEVICE_SIZES
        ]
        pull_classes = [
            self.get_offset_class(device)
            for device in self.DEVICE_SIZES
        ]
        classes = size_classes + offset_classes + push_classes + pull_classes
        return ' '.join(html_class for html_class in classes if html_class)

for size, name in constants.DEVICE_CHOICES:
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_col'.format(size),
        ColSizeField(verbose_name=_('col-{}-'.format(size))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_offset'.format(size),
        OffsetSizeField(verbose_name=_('offset-{}-'.format(size))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_push'.format(size),
        PushSizeField(verbose_name=_('push-{}-'.format(size))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_pull'.format(size),
        PullSizeField(verbose_name=_('pull-{}-'.format(size))),
    )

