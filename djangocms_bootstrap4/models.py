# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
import collections

from functools import partial

import django.forms.models
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.utils.translation import ugettext, ugettext_lazy as _, ungettext

import cms.models
import cms.models.fields
from cms.models.pluginmodel import CMSPlugin

import filer.fields.file
import filer.fields.image
import filer.fields.folder

import djangocms_text_ckeditor.fields
from djangocms_attributes_field.fields import AttributesField

from . import model_fields, constants


# CSS - http://getbootstrap.com/css/
# Global CSS settings, fundamental HTML elements styled and enhanced with
# extensible classes, and an advanced grid system.
#
# The following components marked with "✓" are implemented:
#
# [✓] Grid
# [✓] Typography (Blockquote and Cite)
# [✓] Code
# [✓] Forms (via aldryn-forms)
# [✓] Buttons
# [✓] Images
# [✓] Helper classes (js/ckeditor.js)
# [✓] Responsive utilities


@python_2_unicode_compatible
class Bootstrap3RowPlugin(CMSPlugin):
    """
    CSS - Grid system: "Row" Model
    http://getbootstrap.com/css/#grid
    """
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        instance = self.get_plugin_instance()[0]

        if not instance:
            return ugettext('<empty>')

        column_count = len(self.child_plugin_instances or [])
        column_count_str = ungettext(
            '1 column',
            '%(count)i columns',
            column_count
        ) % {'count': column_count}

        if self.classes:
            return '{} ({})'.format(
                self.classes,
                column_count_str
            )
        return column_count_str


@python_2_unicode_compatible
class Bootstrap3ColumnPlugin(CMSPlugin):
    """
    CSS - Grid system: "Column" Model
    http://getbootstrap.com/css/#grid
    """
    tag = models.SlugField(
        verbose_name=_('Tag'),
        default='div',
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

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
        for device in constants.DEVICE_SIZES:
            for element in ('col', 'offset', 'push', 'pull'):
                classes.append(self.get_class(device, element))
        return ' '.join(cls for cls in classes if cls)


ColSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default=None,
    min_value=1,
    max_value=constants.GRID_SIZE,
)

OffsetSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default=None,
    min_value=0,
    max_value=constants.GRID_SIZE,
)

PushSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default=None,
    min_value=0,
    max_value=constants.GRID_SIZE,
)

PullSizeField = partial(
    model_fields.IntegerField,
    null=True,
    blank=True,
    default=None,
    min_value=0,
    max_value=constants.GRID_SIZE,
)

for size, name in constants.DEVICE_CHOICES:
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_col'.format(size),
        ColSizeField(verbose_name='col-{}-'.format(size)),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_offset'.format(size),
        OffsetSizeField(verbose_name='offset-'.format(size)),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_push'.format(size),
        PushSizeField(verbose_name='push-'.format(size)),
    )
    Bootstrap3ColumnPlugin.add_to_class(
        '{}_pull'.format(size),
        PullSizeField(verbose_name='pull-'.format(size)),
    )


@python_2_unicode_compatible
class Boostrap3BlockquotePlugin(CMSPlugin):
    """
    CSS - Typography: "Blockquote" Model
    http://getbootstrap.com/css/#type-blockquotes
    """
    reverse = models.BooleanField(
        verbose_name=_('Reverse quote'),
        default=False,
        blank=True,
        help_text=_('Reverses the position by adding the Bootstrap 3 '
                    '"blockquote-reverse" class.'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        if self.reverse:
            return '.blockquote-reverse'
        return ''


@python_2_unicode_compatible
class Boostrap3CitePlugin(CMSPlugin):
    """
    CSS - Typography: "Cite" Model
    http://getbootstrap.com/css/#type-blockquotes
    """
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return ''


@python_2_unicode_compatible
class Bootstrap3CodePlugin(CMSPlugin):
    """
    CSS - Code: Model
    http://getbootstrap.com/css/#code
    """
    CODE_TYPE_CHOICES = (
        ('code', _('Inline')),
        ('kbd', _('User input')),
        ('pre', _('Basic block')),
        ('var', _('Variables')),
        ('samp', _('Sample output')),
    )

    code_type = models.CharField(
        verbose_name=_('Code type'),
        choices=CODE_TYPE_CHOICES,
        default=CODE_TYPE_CHOICES[0][0],
        max_length=255,
    )
    code = models.TextField(
        verbose_name=_('Code'),
        blank=True,
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return '<{}>'.format(self.code_type)


@python_2_unicode_compatible
class Boostrap3ButtonPlugin(CMSPlugin, model_fields.LinkMixin):
    """
    CSS - Buttons: "Button/Link" Model
    http://getbootstrap.com/css/#buttons
    """
    label = models.CharField(
        verbose_name=_('Display name'),
        blank=True,
        default='',
        max_length=255,
    )
    type = model_fields.LinkOrButton(
        verbose_name=_('Type'),
    )
    # button specific fields
    btn_context = model_fields.Context(
        verbose_name=_('Context'),
        choices=constants.BUTTON_CONTEXT_CHOICES,
        default=constants.BUTTON_CONTEXT_DEFAULT,
    )
    btn_size = model_fields.Size(
        verbose_name=_('Size'),
    )
    btn_block = models.BooleanField(
        verbose_name=_('Block'),
        default=False,
    )
    # text link specific fields
    txt_context = model_fields.Context(
        verbose_name=_('Context'),
        choices=constants.TEXT_LINK_CONTEXT_CHOICES,
        default=constants.TEXT_LINK_CONTEXT_DEFAULT,
        blank=True,
    )
    # common fields
    icon_left = model_fields.Icon(
        verbose_name=_('Icon left'),
    )
    icon_right = model_fields.Icon(
        verbose_name=_('Icon right'),
    )
    classes = model_fields.Classes()

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Boostrap3ImagePlugin(CMSPlugin):
    """
    CSS - Images: Model
    http://getbootstrap.com/css/#images
    """
    file = filer.fields.image.FilerImageField(
        verbose_name=_('Image'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    alt = model_fields.MiniText(
        verbose_name=_('Alternative text'),
        blank=True,
        default='',
    )
    title = model_fields.MiniText(
        verbose_name=_('Title'),
        blank=True,
        default='',
    )
    use_original_image = models.BooleanField(
        verbose_name=_('Use original image'),
        blank=True,
        default=False,
        help_text=_('Outputs the raw image without cropping.')
    )
    override_width = models.IntegerField(
        verbose_name=_('Override width'),
        blank=True,
        null=True,
        help_text=_('The image width as number in pixels. '
                    'Example: "720" and not "720px".'),
    )
    override_height = models.IntegerField(
        verbose_name=_('Override height'),
        blank=True,
        null=True,
        help_text=_('The image height as number in pixels. '
                    'Example: "720" and not "720px".'),
    )
    aspect_ratio = models.CharField(
        verbose_name=_('Aspect ratio'),
        choices=constants.ASPECT_RATIO_CHOICES,
        blank=True,
        default='',
        max_length=255,
        help_text=_('Determines width and height of the image '
                    'according to the selected ratio.'),
    )
    shape = models.CharField(
        verbose_name=_('Shape'),
        choices=(
            ('rounded', '.img-rounded'),
            ('circle', '.img-circle'),
        ),
        default='',
        blank=True,
        max_length=255,
    )
    thumbnail = models.BooleanField(
        verbose_name='.img-thumbnail',
        default=False,
        blank=True,
        help_text=_('Adds the Bootstrap 3 ".img-thumbnail" class.'),
    )
    img_responsive = models.BooleanField(
        verbose_name='.img-responsive',
        default=True,
        blank=True,
        help_text=_('Adds the Bootstrap 3 ".img-responsive" class.')
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['src', 'alt', 'class', 'title'],
    )
    classes = model_fields.Classes()

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        txt = ''
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
                'size_str': '{}x{}'.format(width, height),
                'width_str': '{}w'.format(width),
                'subject_location': self.file.subject_location,
                'upscale': True,
                'crop': crop,
                'aspect_ratio': (aspect_width, aspect_height),
                'width_tag': width_tag,
            }

        return items


@python_2_unicode_compatible
class Bootstrap3ResponsivePlugin(CMSPlugin):
    """
    CSS - Responsive: "Utilities" Model
    http://getbootstrap.com/css/#responsive-utilities
    """
    device_breakpoints = model_fields.Responsive(
        verbose_name=_('Devices'),
        default='visible-xs visible-sm visible-md visible-lg',
    )
    print_breakpoints = model_fields.ResponsivePrint(
        verbose_name=_('Print'),
        default='visible-print',
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        text = self.device_breakpoints
        if self.print_breakpoints:
            text += ' {}'.format(self.print_breakpoints)
        return text


# Components - http://getbootstrap.com/components/
# Over a dozen reusable components built to provide iconography, dropdowns,
# input groups, navigation, alerts, and much more.
#
# The following components marked with "✓" are implemented:
#
# [✓] Glyphicons
# [ ] Dropdowns
# [ ] Button Groups
# [ ] Button Dropdowns
# [✓] Input Groups (via aldryn-forms)
# [✗] Navs (not applicable)
# [✗] Navbar (not applicable)
# [✗] Breadcrumbs (not applicable)
# [✗] Pagination (not applicable)
# [✓] Labels
# [✗] Badges (not applicable)
# [✓] Jumbotron
# [ ] Page header
# [ ] Thumbnails
# [✓] Alerts
# [ ] Progress Bars
# [ ] Media object
# [✓] List Group
# [✓] Panels
# [ ] Responsive embed
# [✓] Wells


@python_2_unicode_compatible
class Boostrap3IconPlugin(CMSPlugin):
    """
    Component - Glyphicons: "Icon" Model
    http://getbootstrap.com/components/#glyphicons
    Component - Font Awesome: "Icon" Model
    http://fontawesome.io/
    """
    icon = model_fields.Icon(
        verbose_name=_('Icon'),
        blank=False,
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.icon


@python_2_unicode_compatible
class Boostrap3LabelPlugin(CMSPlugin):
    """
    Component - Label: Model
    http://getbootstrap.com/components/#labels
    """
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        default='',
        max_length=255,
    )
    context = model_fields.Context(
        verbose_name=_('Context'),
        choices=(
            ('default', _('Default')),
        ) + constants.CONTEXT_CHOICES,
        default='default',
        blank=False,
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Boostrap3JumbotronPlugin(CMSPlugin):
    """
    Component - Jumbotron: Model
    http://getbootstrap.com/components/#jumbotron
    """
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
    )
    grid = models.BooleanField(
        verbose_name=_('Add container'),
        default=False,
        blank=True,
        help_text=_('Adds a ".container" element inside the "Jumbotron" '
                    'for use outside of a grid.'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.label or str(self.pk)


@python_2_unicode_compatible
class Boostrap3AlertPlugin(CMSPlugin):
    """
    Component - Alert: Model
    http://getbootstrap.com/components/#alerts
    """
    context = model_fields.Context(
        verbose_name=_('Context'),
    )
    icon = model_fields.Icon(
        verbose_name=_('Title icon'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.classes


class Bootstrap3ListGroupPlugin(CMSPlugin):
    """
    Component - List group: "Wrapper" Model
    http://getbootstrap.com/components/#alerts
    """
    add_list_group_class = models.BooleanField(
        verbose_name='.list-group',
        default=True,
        blank=True,
        help_text=_('Adds the list-group and subsequent list-group-item classes.'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def get_short_description(self):
        instance = self.get_plugin_instance()[0]

        if not instance:
            return ugettext('<empty>')

        column_count = len(self.child_plugin_instances or [])
        column_count_str = ungettext(
            '1 item',
            '%(count)i items',
            column_count
        ) % {'count': column_count}
        return column_count_str


@python_2_unicode_compatible
class Bootstrap3ListGroupItemPlugin(CMSPlugin):
    """
    Component - List group: "Item" Model
    http://getbootstrap.com/components/#alerts
    """
    title = model_fields.MiniText(
        verbose_name=_('Title'),
        blank=True,
        default='',
    )
    context = model_fields.Context(
        verbose_name=_('Context'),
        choices=(
            ('default', _('Default')),
        ) + constants.CONTEXT_CHOICES,
        default='default',
        blank=False,
    )
    state = models.CharField(
        verbose_name=_('State'),
        choices=(
            ('active', _('Active')),
            ('disabled', _('Disabled')),
        ),
        blank=True,
        max_length=255,
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Boostrap3PanelPlugin(CMSPlugin):
    """
    Component - Panel: "Wrapper" Model
    http://getbootstrap.com/components/#panels
    """
    context = model_fields.Context(
        verbose_name=_('Context'),
        choices=(
            ('default', _('Default')),
        ) + constants.CONTEXT_CHOICES,
        default='default',
        blank=False,
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.context


@python_2_unicode_compatible
class Boostrap3PanelHeadingPlugin(CMSPlugin):
    """
    Component - Panel: "Heading" Model
    http://getbootstrap.com/components/#panels-heading
    """
    title = model_fields.MiniText(
        verbose_name=_('Title'),
        blank=True,
        default='',
        help_text=_('Panels can have additional plugins.')
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Boostrap3PanelBodyPlugin(CMSPlugin):
    """
    Component - Panel: "Body" Model
    http://getbootstrap.com/components/#panels
    """
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.classes


@python_2_unicode_compatible
class Boostrap3PanelFooterPlugin(CMSPlugin):
    """
    Component - Panel: "Footer" Model
    http://getbootstrap.com/components/#panels-footer
    """
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.classes


@python_2_unicode_compatible
class Boostrap3WellPlugin(CMSPlugin):
    """
    Component - Wells: Model
    http://getbootstrap.com/components/#wells
    """
    size = model_fields.Size(
        verbose_name=_('Size'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.classes


# JavaScript - http://getbootstrap.com/javascript/
# Bring Bootstrap's components to life with over a dozen custom jQuery plugins.
# Easily include them all, or one by one.
#
# The following components marked with "✓" are implemented:
#
# [x] Transitions (not applicable)
# [ ] Modal
# [ ] Dropdowns
# [ ] Scrollspy
# [✓] Tab
# [ ] Tooltip
# [ ] Popover
# [ ] Alert
# [ ] Button
# [✓] Collapse
# [✓] Carousel
# [ ] Affix


@python_2_unicode_compatible
class Bootstrap3TabPlugin(CMSPlugin):
    """
    JavaScript - Tab: "Wrapper" Model
    http://getbootstrap.com/javascript/#tabs
    """
    TAB_TYPE_CHOICES = (
        ('nav-tabs', _('Tabs')),
        ('nav-tabs nav-justified', _('Tabs justified')),
        ('nav-pills', _('Pills')),
        ('nav-pills nav-justified', _('Pills justified')),
    )
    TAB_EFFECT_CHOICES = (
        ('fade', _('Fade')),
    )

    index = models.PositiveIntegerField(
        verbose_name=_('Index'),
        null=True,
        blank=True,
        help_text=_('Index of element to open on page load (optional).'),
    )
    style = models.CharField(
        verbose_name=_('Display type'),
        choices=TAB_TYPE_CHOICES,
        default=TAB_TYPE_CHOICES[0][0],
        max_length=255,
    )
    effect = models.CharField(
        verbose_name=_('Animation effect'),
        choices=TAB_EFFECT_CHOICES,
        blank=True,
        max_length=255,
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return '{} {}'.format(self.style, self.effect)


@python_2_unicode_compatible
class Bootstrap3TabItemPlugin(CMSPlugin):
    """
    JavaScript - Tab: "Item" Model
    http://getbootstrap.com/javascript/#tabs
    """
    title = models.CharField(
        verbose_name=_('Tab title'),
        max_length=255,
    )
    icon = model_fields.Icon(
        verbose_name=_('Title icon'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Bootstrap3AccordionPlugin(CMSPlugin):
    """
    JavaScript - Collapse: "Accordion" Model
    http://getbootstrap.com/javascript/#collapse
    """
    index = models.PositiveIntegerField(
        verbose_name=_('Index'),
        null=True,
        blank=True,
        help_text=_('Index of element to open on page load (optional).'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def get_short_description(self):
        instance = self.get_plugin_instance()[0]

        if not instance:
            return ugettext('<empty>')

        column_count = len(self.child_plugin_instances or [])
        column_count_str = ungettext(
            '1 item',
            '%(count)i items',
            column_count
        ) % {'count': column_count}
        return column_count_str

    def __str__(self):
        return str(self.index)


@python_2_unicode_compatible
class Bootstrap3AccordionItemPlugin(CMSPlugin):
    """
    JavaScript - Collapse: "Accordion item" Model
    http://getbootstrap.com/javascript/#collapse
    """
    title = model_fields.MiniText(
        verbose_name=_('Title'),
        default='',
        blank=True,
    )
    context = model_fields.Context(
        verbose_name=_('Context'),
        choices=(
            ('default', _('Default')),
        ) + constants.CONTEXT_CHOICES,
        default='default',
        blank=False,
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Bootstrap3CarouselPlugin(CMSPlugin):
    """
    JavaScript - Carousel: "Wrapper" Model
    http://getbootstrap.com/javascript/#carousel
    """
    STYLE_DEFAULT = 'standard'
    STYLE_CHOICES = [
        (STYLE_DEFAULT, _('Standard')),
    ]
    TRANSITION_EFFECT_CHOICES = (
        ('slide', _('Slide')),
    )

    style = models.CharField(
        verbose_name=_('Style'),
        choices=STYLE_CHOICES + model_fields.get_additional_styles(),
        default=STYLE_DEFAULT,
        max_length=255,
    )
    aspect_ratio = models.CharField(
        verbose_name=_('Aspect ratio'),
        choices=constants.ASPECT_RATIO_CHOICES,
        blank=True,
        default='',
        max_length=255,
        help_text=_('Determines width and height of the image '
                    'according to the selected ratio.'),
    )
    transition_effect = models.CharField(
        verbose_name=_('Transition effect'),
        choices=TRANSITION_EFFECT_CHOICES,
        default='',
        blank=True,
        max_length=255,
    )
    ride = models.BooleanField(
        verbose_name=_('Ride'),
        default=True,
        help_text=_('Auto-starts animation of the carousel.'),
    )
    interval = models.IntegerField(
        verbose_name=_('Interval'),
        default=5000,
        help_text=_('Time (in milliseconds) between items.'),
    )
    wrap = models.BooleanField(
        verbose_name=_('Wrap'),
        default=True,
        blank=True,
        help_text=_('Loops carousel animation.'),
    )
    pause = models.BooleanField(
        verbose_name=_('Pause'),
        default=True,
        blank=True,
        help_text=_('Pauses the carousel on hover.'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=[
            'class',
            # data attributes et via settings
            'data-ride', 'data-interval', 'data-pause', 'data-wrap'
        ],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        data = django.forms.models.model_to_dict(self)
        data.update(dict(
            style_label=_('Style'),
            transition_effect_label=_('Transition effect'),
            ride_label=_('Ride'),
            interval_label=_('Interval'),
            aspect_ratio_label=_('Aspect ratio'),
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
                'size_str': '{}x{}'.format(width, height),
                'width_str': '{}w'.format(width),
                # 'subject_location': self.file.subject_location,
                'upscale': True,
                'crop': crop,
                'aspect_ratio': (aspect_width, aspect_height),
                'width_tag': width_tag,
            }

        return items


@python_2_unicode_compatible
class Bootstrap3CarouselSlidePlugin(CMSPlugin, model_fields.LinkMixin):
    """
    JavaScript - Carousel: "Slide" Model
    http://getbootstrap.com/javascript/#carousel
    """
    image = filer.fields.image.FilerImageField(
        verbose_name=_('Image'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    link_text = models.CharField(
        verbose_name=_('Link text'),
        max_length=255,
        blank=True,
    )
    content = djangocms_text_ckeditor.fields.HTMLField(
        verbose_name=_('Content'),
        blank=True,
        default='',
        help_text=_('Content may also be added using child plugins.'),
    )
    classes = model_fields.Classes()

    cmsplugin_ptr = model_fields.CMSPluginField()

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
    """
    JavaScript - Carousel: "Slide folder" Model
    http://getbootstrap.com/javascript/#carousel
    """
    folder = filer.fields.folder.FilerFolderField(
        verbose_name=_('Folder'),
    )
    classes = model_fields.Classes()

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        if self.folder_id:
            return self.folder.pretty_logical_path
        else:
            return _('<folder is missing>')


# Custom plugins added to support further stylings
#
# [✓] Spacer
# [✓] File


@python_2_unicode_compatible
class Boostrap3SpacerPlugin(CMSPlugin):
    """
    Custom - Spacer: Model
    """
    size = model_fields.Size(
        verbose_name=_('Size'),
    )
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        return 'size-' + self.size + ' ' + self.classes


@python_2_unicode_compatible
class Bootstrap3FilePlugin(CMSPlugin):
    """
    Custom - File: Model
    """
    file = filer.fields.file.FilerFileField(
        verbose_name=_('File'),
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    name = model_fields.MiniText(
        verbose_name=_('Name'),
        default='',
        blank=True,
    )
    open_new_window = models.BooleanField(
        verbose_name=_('Open in new window'),
        default=False,
    )
    show_file_size = models.BooleanField(
        verbose_name=_('Show file size'),
        default=False,
    )
    # common fields
    icon_left = model_fields.Icon()
    icon_right = model_fields.Icon()
    # additional fields
    classes = model_fields.Classes()
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class', 'target'],
    )

    cmsplugin_ptr = model_fields.CMSPluginField()

    def __str__(self):
        label = self.name
        if not label:
            if self.file_id:
                label = self.file.label
            else:
                label = 'File'
        return label
