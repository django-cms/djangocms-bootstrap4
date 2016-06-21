# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from functools import partial
import collections

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _, ungettext

import django.forms.models

from cms.models.pluginmodel import CMSPlugin
import cms.models
import cms.models.fields

from djangocms_attributes_field.fields import AttributesField
import djangocms_text_ckeditor.fields
import filer.fields.file
import filer.fields.image
import filer.fields.folder

from . import model_fields, constants, utils


##########
# Mixins #  do NOT use outside of this package!
##########  Because changes here might require Database migrations!
import os


class LinkMixin(models.Model):
    link_url = models.URLField(_("link"), blank=True, default='')
    link_page = cms.models.fields.PageField(
        verbose_name=_("page"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    link_file = filer.fields.file.FilerFileField(
        verbose_name=_("file"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    link_anchor = models.CharField(
        _("anchor"), max_length=128, blank=True,
        help_text=_("Adds this value as an anchor (#my-anchor) to the link."),
    )
    link_mailto = models.EmailField(
        _("mailto"), blank=True, null=True, max_length=254
    )
    link_phone = models.CharField(
        _('Phone'), blank=True, null=True, max_length=40,
    )
    link_target = models.CharField(
        _("target"), blank=True, max_length=100,
        choices=((
            ("", _("same window")),
            ("_blank", _("new window")),
            ("_parent", _("parent window")),
            ("_top", _("topmost frame")),
        ))
    )
    # Override this property in concrete classes as required.
    excluded_attr_keys = ['href', 'target', ]
    link_attributes = AttributesField(_('Link Attributes'), excluded_keys=excluded_attr_keys)

    class Meta:
        abstract = True

    def get_link_url(self):
        if self.link_phone:
            link = u"tel://{0}".format(self.link_phone).replace(' ', '')
        elif self.link_mailto:
            link = u"mailto:{0}".format(self.link_mailto)
        elif self.link_url:
            link = self.link_url
        elif self.link_page_id:
            link = self.link_page.get_absolute_url()
        elif self.link_file:
            link = self.link_file.url
        else:
            link = ""
        if self.link_anchor:
            link += '#{0}'.format(self.link_anchor)
        return link


#################
# Basic Plugins #
#################

@python_2_unicode_compatible
class Boostrap3ButtonPlugin(CMSPlugin, LinkMixin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)
    excluded_attr_keys = ['class', 'href', 'target', ]

    label = models.CharField(
        _("label"),
        max_length=256,
        blank=True,
        default='',
    )
    type = model_fields.LinkOrButton()

    # button specific fields
    btn_context = model_fields.Context(
        verbose_name='context',
        choices=constants.BUTTON_CONTEXT_CHOICES,
        default=constants.BUTTON_CONTEXT_DEFAULT,
    )
    btn_size = model_fields.Size(verbose_name='size')
    btn_block = models.BooleanField(default=False, verbose_name='block')
    # text link specific fields
    txt_context = model_fields.Context(
        verbose_name='context',
        choices=constants.TXT_LINK_CONTEXT_CHOICES,
        default=constants.TXT_LINK_CONTEXT_DEFAULT,
        blank=True,
    )
    # common fields
    icon_left = model_fields.Icon()
    icon_right = model_fields.Icon()

    classes = model_fields.Classes()
    responsive = model_fields.Responsive(
        blank=True,
        default='',
    )
    responsive_print = model_fields.ResponsivePrint(
        blank=True,
        default='',
    )

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
class Boostrap3IconPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    icon = model_fields.Icon(blank=False)

    classes = model_fields.Classes()

    def __str__(self):
        return self.icon


@python_2_unicode_compatible
class Boostrap3LabelPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    label = models.CharField(
        _("label"),
        max_length=256,
        blank=True,
        default='',
    )
    context = model_fields.Context(
        choices=constants.LABEL_CONTEXT_CHOICES,
        default=constants.LABEL_CONTEXT_DEFAULT,
        blank=False,
    )

    classes = model_fields.Classes()

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Boostrap3WellPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    size = model_fields.Size()

    classes = model_fields.Classes()

    def __str__(self):
        return self.classes


@python_2_unicode_compatible
class Boostrap3AlertPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    context = model_fields.Context()
    icon = model_fields.Icon()

    classes = model_fields.Classes()

    def __str__(self):
        return self.classes


def compute_aspect_ratio(image):
    if image.exif.get('Orientation', 1) > 4:
        # image is rotated by 90 degrees, while keeping width and height
        return float(image.width) / float(image.height)
    else:
        return float(image.height) / float(image.width)


@python_2_unicode_compatible
class Boostrap3ImagePlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    file = filer.fields.image.FilerImageField(
        verbose_name=_("file"),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    alt = model_fields.MiniText(
        _("alt"),
        blank=True,
        default='',
    )
    title = model_fields.MiniText(
        _("title"),
        blank=True,
        default='',
    )
    use_original_image = models.BooleanField(
        _("use original image"),
        blank=True,
        default=False,
        help_text=_(
            "use the original full-resolution image (no resizing)."
        )
    )
    override_width = models.IntegerField(
        _("override width"),
        blank=True,
        null=True,
        help_text=_(
            'if this field is provided it will be used to scale image.'
        )
    )
    override_height = models.IntegerField(
        _("override height"),
        blank=True,
        null=True,
        help_text=_(
            'if this field is provided it will be used to scale image. '
            'If aspect ration is selected - height will be calculated '
            'based on that.'
        )
    )
    aspect_ratio = models.CharField(
        _("aspect ratio"),
        max_length=10,
        blank=True,
        default='',
        choices=constants.ASPECT_RATIO_CHOICES
    )
    thumbnail = models.BooleanField(
        _("thumbnail"),
        default=False,
        blank=True,
        help_text="add the 'thumbnail' border",
    )
    shape = models.CharField(
        _('shape'),
        max_length=64,
        blank=True,
        default='',
        choices=(
            ('rounded', 'rounded'),
            ('circle', 'circle'),
        )
    )

    classes = model_fields.Classes()
    img_responsive = models.BooleanField(
        verbose_name='class: img-responsive',
        default=True,
        blank=True,
        help_text='whether to treat the image as using 100% width of the '
                  'parent container (sets the img-responsive class).'
    )

    def __str__(self):
        txt = 'Image'

        if self.file_id and self.file.label:
            txt = self.file.label
        return txt

    def srcset(self):
        if not self.file:
            return []
        items = collections.OrderedDict()
        if self.aspect_ratio:
            aspect_width, aspect_height = tuple([int(i) for i in self.aspect_ratio.split('x')])
        else:
            aspect_width, aspect_height = None, None
        for device in constants.DEVICES:
            if self.override_width:
                width = self.override_width
            else:
                # TODO: should this should be based on the containing col size?
                width = device['width_gutter']
            width_tag = str(width)
            if aspect_width is not None and aspect_height is not None:
                height = int(float(width)*float(aspect_height)/float(aspect_width))
                crop = True
            else:
                if self.override_height:
                    height = self.override_height
                else:
                    height = 0
                crop = False
            items[device['identifier']] = {
                'size': (width, height),
                'size_str': "{}x{}".format(width, height),
                'width_str': "{}w".format(width),
                'subject_location': self.file.subject_location,
                'upscale': True,
                'crop': crop,
                'aspect_ratio': (aspect_width, aspect_height),
                'width_tag': width_tag,
            }

        return items


@python_2_unicode_compatible
class Boostrap3SpacerPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    size = model_fields.Size()

    classes = model_fields.Classes()

    def __str__(self):
        return 'size-' + self.size + ' ' + self.classes


@python_2_unicode_compatible
class Bootstrap3FilePlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    file = filer.fields.file.FilerFileField(
        verbose_name=_("file"),
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    name = model_fields.MiniText(
        _("name"),
        blank=True,
        default='',
    )
    open_new_window = models.BooleanField(default=False)
    show_file_size = models.BooleanField(default=False)

    # common fields
    icon_left = model_fields.Icon()
    icon_right = model_fields.Icon()

    classes = model_fields.Classes()

    def __str__(self):
        label = self.name
        if not label:
            if self.file_id:
                label = self.file.label
            else:
                label = 'File'
        return label


#########
# Panel #
#########


@python_2_unicode_compatible
class Boostrap3PanelPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    context = model_fields.Context(
        choices=constants.PANEL_CONTEXT_CHOICES,
        default=constants.PANEL_CONTEXT_DEFAULT,
        blank=False,
    )

    classes = model_fields.Classes()

    def __str__(self):
        return self.context


@python_2_unicode_compatible
class Boostrap3PanelHeadingPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    title = model_fields.MiniText(
        _("title"),
        blank=True,
        default='',
        help_text='Alternatively you can add plugins'
    )

    classes = model_fields.Classes()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Boostrap3PanelBodyPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    classes = model_fields.Classes()

    def __str__(self):
        return self.classes


@python_2_unicode_compatible
class Boostrap3PanelFooterPlugin(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    classes = model_fields.Classes()

    def __str__(self):
        return self.classes


########
# Grid #
########

ColSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default=None,
    min_value=1,
    max_value=constants.GRID_SIZE
)

OffsetSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default=None,
    min_value=0,
    max_value=constants.GRID_SIZE
)

PushSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default=None,
    min_value=0,
    max_value=constants.GRID_SIZE
)

PullSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default=None,
    min_value=0,
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
        size = getattr(self, '{}_{}'.format(device, element), None)
        if size is not None:
            if element == 'col':
                return 'col-{}-{}'.format(device, size)
            else:
                return 'col-{}-{}-{}'.format(device, element, size)
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
        OffsetSizeField(verbose_name=_('offset-'.format(size))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_push'.format(size),
        PushSizeField(verbose_name=_('push-'.format(size))),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_pull'.format(size),
        PullSizeField(verbose_name=_('pull-'.format(size))),
    )



#############
# Accordion #
#############

@python_2_unicode_compatible
class Bootstrap3AccordionPlugin(CMSPlugin):
    index = models.PositiveIntegerField(
        _('index'), null=True, blank=True,
        help_text=_('index of element that should be opened on page load '
                    '(leave it empty if none of the items should be opened)'))
    classes = model_fields.Classes()

    def __str__(self):
        return _("%s items") % self.cmsplugin_set.all().count()


@python_2_unicode_compatible
class Bootstrap3AccordionItemPlugin(CMSPlugin):
    title = model_fields.MiniText(
        _("title"),
        blank=True,
        default='',
    )
    context = model_fields.Context(
        choices=constants.ACCORDION_ITEM_CONTEXT_CHOICES,
        default=constants.ACCORDION_ITEM_CONTEXT_DEFAULT,
        blank=False,
    )

    classes = model_fields.Classes()

    def __str__(self):
        return self.title


#############
# ListGroup #
#############

@python_2_unicode_compatible
class Bootstrap3ListGroupPlugin(CMSPlugin):
    classes = model_fields.Classes()
    add_list_group_class = models.BooleanField(
        verbose_name='class: list-group',
        default=True,
        blank=True,
        help_text='whether to add the list-group and list-group-item classes'
    )

    def __str__(self):
        return _("%s items") % self.cmsplugin_set.all().count()


@python_2_unicode_compatible
class Bootstrap3ListGroupItemPlugin(CMSPlugin):
    title = model_fields.MiniText(
        _("title"),
        blank=True,
        default='',
    )
    context = model_fields.Context(
        choices=constants.LIST_GROUP_ITEM_CONTEXT_CHOICES,
        default=constants.LIST_GROUP_ITEM_CONTEXT_DEFAULT,
        blank=True,
    )
    state = models.CharField(
        verbose_name='state',
        choices=(
            ('active', 'active'),
            ('disabled', 'disabled'),
        ),
        max_length=255,
        blank=True,
    )

    classes = model_fields.Classes()

    def __str__(self):
        return self.title


############
# Carousel #  derived from https://github.com/aldryn/aldryn-gallery/tree/0.2.6
############

@python_2_unicode_compatible
class Bootstrap3CarouselPlugin(CMSPlugin):
    STYLE_DEFAULT = 'standard'

    STYLE_CHOICES = [
        (STYLE_DEFAULT, _('Standard')),
    ]

    TRANSITION_EFFECT_CHOICES = (
        ('slide', _('Slide')),
    )

    style = models.CharField(
        _('Style'),
        choices=STYLE_CHOICES + utils.get_additional_styles(),
        default=STYLE_DEFAULT,
        max_length=50,
    )
    aspect_ratio = models.CharField(
        _("aspect ratio"),
        max_length=10,
        blank=True,
        default='',
        choices=constants.ASPECT_RATIO_CHOICES
    )
    transition_effect = models.CharField(
        _('Transition Effect'),
        choices=TRANSITION_EFFECT_CHOICES,
        default='',
        max_length=50,
        blank=True,
    )
    ride = models.BooleanField(
        _('Ride'),
        default=True,
        help_text=_('Whether to mark the carousel as animating '
                    'starting at page load.'),
    )
    interval = models.IntegerField(
        _('Interval'),
        default=5000,
        help_text=_("The amount of time to delay between automatically "
                    "cycling an item."),
    )
    wrap = models.BooleanField(
        default=True,
        blank=True,
        help_text=_('Whether the carousel should cycle continuously or '
                    'have hard stops.')
    )
    pause = models.BooleanField(
        default=True,
        blank=True,
        help_text=_('Pauses the cycling of the carousel on mouseenter and '
                    'resumes the cycling of the carousel on mouseleave.')
    )
    classes = model_fields.Classes()

    def __str__(self):
        data = django.forms.models.model_to_dict(self)
        data.update(dict(
            style_label=_('Style'),
            transition_effect_label=_('Transition Effect'),
            ride_label=_('Ride'),
            interval_label=_('Interval'),
            aspect_ratio_label=_('Aspect Ratio'),
        ))
        fields = [
            'style',
            'transition_effect',
            'ride',
            'interval',
            'aspect_ratio',
        ]
        if not data['ride']:
            fields.remove('interval')
        return ', '.join([
            '{key}: {value}'.format(
                key=data['{}_label'.format(field)],
                value=data[field]
            ) for field in fields
        ])

    def srcset(self):
        # more or less copied from image plugin.
        # TODO: replace with generic sizes/srcset solution
        items = collections.OrderedDict()
        if self.aspect_ratio:
            aspect_width, aspect_height = tuple([int(i) for i in self.aspect_ratio.split('x')])
        else:
            aspect_width, aspect_height = None, None
        for device in constants.DEVICES:
            width = device['width_gutter']  # TODO: should this should be based on the containing col size?
            width_tag = str(width)
            if aspect_width is not None and aspect_height is not None:
                height = int(float(width)*float(aspect_height)/float(aspect_width))
                crop = True
            else:
                height = 0
                crop = False
            items[device['identifier']] = {
                'size': (width, height),
                'size_str': "{}x{}".format(width, height),
                'width_str': "{}w".format(width),
                # 'subject_location': self.file.subject_location,
                'upscale': True,
                'crop': crop,
                'aspect_ratio': (aspect_width, aspect_height),
                'width_tag': width_tag,
            }

        return items

@python_2_unicode_compatible
class Bootstrap3CarouselSlidePlugin(CMSPlugin, LinkMixin):
    excluded_attr_keys = ['class', 'href', 'target', ]
    image = filer.fields.image.FilerImageField(
        verbose_name=_('image'),
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    link_text = models.CharField(
        verbose_name=_('link text'),
        max_length=200,
        blank=True
    )
    content = djangocms_text_ckeditor.fields.HTMLField(
        _("Content"),
        blank=True,
        default='',
        help_text=_('alternatively add sub plugins as content'),
    )
    classes = model_fields.Classes()

    def __str__(self):
        image_text = content_text = ''

        if self.image_id:
            if self.image.name:
                image_text = self.image.name
            elif self.image.original_filename \
                    and os.path.split(self.image.original_filename)[1]:
                image_text = os.path.split(self.image.original_filename)[1]
            else:
                image_text = 'Image'
        if self.content:
            text = strip_tags(self.content).strip()
            if len(text) > 100:
                content_text = '{}...'.format(text[:100])
            else:
                content_text = '{}'.format(text)

        if image_text and content_text:
            return '{} ({})'.format(image_text, content_text)
        else:
            return image_text or content_text

@python_2_unicode_compatible
class Bootstrap3CarouselSlideFolderPlugin(CMSPlugin):
    folder = filer.fields.folder.FilerFolderField(
        verbose_name=_('folder'),
    )
    classes = model_fields.Classes()

    def __str__(self):
        if self.folder:
            return self.folder.pretty_logical_path
        else:
            return _('not selected yet')
