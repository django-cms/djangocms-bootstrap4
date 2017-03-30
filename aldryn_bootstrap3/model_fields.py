# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from functools import partial

import django.db.models
import django.forms

from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _, ungettext

from django.utils.encoding import force_text

import cms.models
import cms.models.fields
from cms.models.pluginmodel import CMSPlugin

import filer.fields.file
import filer.fields.image

from djangocms_attributes_field.fields import AttributesField

from .conf import settings
from . import fields, constants


def get_additional_styles():
    """
    Get additional styles choices from settings
    """
    choices = []
    raw = getattr(
        settings,
        'ALDRYN_BOOTSTRAP3_CAROUSEL_STYLES',
        getattr(settings, 'GALLERY_STYLES', False)
    )
    if raw:
        if isinstance(raw, str):
            raw = raw.split(',')
            for choice in raw:
                clean = choice.strip()
                choices.append((clean.lower(), clean.title()))
        else:
            for choice in raw:
                choices.append(choice)
    return choices


# Add an app namespace to related_name to avoid field name clashes
# with any other plugins that have a field with the same name as the
# lowercase of the class name of this model.
# https://github.com/divio/django-cms/issues/5030
CMSPluginField = partial(
    models.OneToOneField,
    to=CMSPlugin,
    related_name='%(app_label)s_%(class)s',
    parent_link=True,
)


# Helper for:
# Classes, LinkOrButton, Size, IntegerField
class SouthMixinBase(object):
    south_field_class = ''

    def south_field_triple(self):
        """Returns a suitable description of this field for South."""
        if not self.south_field_class:
            raise NotImplementedError('Please set south_field_class when '
                                        'using the south field mixin.')
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = self.south_field_class
        args, kwargs = introspector(self)
        # That's our definition!
        return field_class, args, kwargs


# Code here is mostly used in `models.py` and `migrations/`


class Classes(django.db.models.TextField, SouthMixinBase):
    default_field_class = fields.Classes
    south_field_class = 'django.db.models.fields.TextField'

    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = _('Classes')
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        if 'default' not in kwargs:
            kwargs['default'] = ''
        if 'help_text' not in kwargs:
            kwargs['help_text'] = _('Space separated classes that are added to '
                'the class. See <a href="http://getbootstrap.com/css/" '
                'target="_blank">Bootstrap 3 documentation</a>.')
        super(Classes, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(Classes, self).formfield(**defaults)


class LinkMixin(models.Model):
    link_url = models.URLField(
        verbose_name=_('External link'),
        blank=True,
        default='',
        help_text=_('Provide a valid URL to an external website.'),
    )
    link_page = cms.models.fields.PageField(
        verbose_name=_('Internal link'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('If provided, overrides the external link.'),
    )
    link_mailto = models.EmailField(
        verbose_name=_('Email address'),
        blank=True,
        null=True,
        max_length=255,
    )
    link_phone = models.CharField(
        verbose_name=_('Phone'),
        blank=True,
        null=True,
        max_length=255,
    )
    link_anchor = models.CharField(
        verbose_name=_('Anchor'),
        max_length=255,
        blank=True,
        help_text=_('Appends the value only after the internal or external link. '
                    'Do <em>not</em> include a preceding "#" symbol.'),
    )
    link_target = models.CharField(
        verbose_name=_('Target'),
        choices=constants.TARGET_CHOICES,
        blank=True,
        max_length=255,
    )
    link_file = filer.fields.file.FilerFileField(
        verbose_name=_('File'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    link_attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class', 'href', 'target'],
    )

    class Meta:
        abstract = True

    def get_link_url(self):
        if self.link_page:
            ref_page = self.link_page
            link = ref_page.get_absolute_url()

            if ref_page.site_id != getattr(self.page, 'site_id', None):
                ref_site = Site.objects._get_site_by_id(ref_page.site_id)
                link = '//{}{}'.format(ref_site, link)
        elif self.link_url:
            link = self.link_url
        elif self.link_phone:
            link = 'tel:{}'.format(self.link_phone.replace(' ', ''))
        elif self.link_mailto:
            link = 'mailto:{}'.format(self.link_mailto)
        elif self.link_file:
            link = self.link_file.url
        else:
            link = ''
        if self.link_anchor:
            link += '#{}'.format(self.link_anchor)
        return link

    def clean(self):
        super(LinkMixin, self).clean()
        field_names = (
            'link_url',
            'link_page',
            'link_mailto',
            'link_phone',
            'link_file',
        )
        anchor_field_name = 'link_anchor'
        field_names_allowed_with_anchor = (
            'link_url',
            'link_page',
            'link_file',
        )

        anchor_field_verbose_name = force_text(
           self._meta.get_field(anchor_field_name).verbose_name)
        anchor_field_value = getattr(self, anchor_field_name)

        link_fields = {
            key: getattr(self, key)
            for key in field_names
        }
        link_field_verbose_names = {
            key: force_text(self._meta.get_field(key).verbose_name)
            for key in link_fields.keys()
        }
        provided_link_fields = {
            key: value
            for key, value in link_fields.items()
            if value
        }

        required_link_classes = (
            'Boostrap3ButtonPlugin',
        )

        if len(provided_link_fields) > 1:
            # Too many fields have a value.
            verbose_names = sorted(link_field_verbose_names.values())
            error_msg = _('Only one of {0} or {1} may be given.').format(
                ', '.join(verbose_names[:-1]),
                verbose_names[-1],
            )
            errors = {}.fromkeys(provided_link_fields.keys(), error_msg)
            raise ValidationError(errors)

        if self.__class__.__name__ in required_link_classes:
            if len(provided_link_fields) == 0 and not self.link_anchor:
               raise ValidationError(
                   _('Please provide a link.')
               )

        if anchor_field_value:
            for field_name in provided_link_fields.keys():
                if field_name not in field_names_allowed_with_anchor:
                    error_msg = _('%(anchor_field_verbose_name)s is not allowed together with %(field_name)s.') % {
                        'anchor_field_verbose_name': anchor_field_verbose_name,
                        'field_name': link_field_verbose_names.get(field_name)
                    }
                    raise ValidationError({
                        anchor_field_name: error_msg,
                        field_name: error_msg,
                    })


class LinkOrButton(django.db.models.fields.CharField, SouthMixinBase):
    default_field_class = fields.LinkOrButton
    south_field_class = 'django.db.models.fields.CharField'

    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = ugettext('Type')
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 255
        if 'blank' not in kwargs:
            kwargs['blank'] = False
        if 'default' not in kwargs:
            kwargs['default'] = self.default_field_class.DEFAULT
        super(LinkOrButton, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
            'choices_form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(LinkOrButton, self).formfield(**defaults)

    def get_choices(self, **kwargs):
        # if there already is a "blank" choice, don't add another
        # default blank choice
        if '' in dict(self.choices).keys():
            kwargs['include_blank'] = False
        return super(LinkOrButton, self).get_choices(**kwargs)


class Context(django.db.models.fields.CharField):
    default_field_class = fields.Context
    south_field_class = 'django.db.models.fields.CharField'

    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = ugettext('Context')
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 255
        if 'blank' not in kwargs:
            kwargs['blank'] = False
        if 'default' not in kwargs:
            kwargs['default'] = self.default_field_class.DEFAULT
        super(Context, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
            'choices_form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(Context, self).formfield(**defaults)

    def get_choices(self, **kwargs):
        # if there already is a "blank" choice, don't add another
        # default blank choice
        if '' in dict(self.choices).keys():
            kwargs['include_blank'] = False
        return super(Context, self).get_choices(**kwargs)


class Icon(django.db.models.CharField):
    default_field_class = fields.Icon
    south_field_class = 'django.db.models.fields.CharField'

    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = ugettext('Icon')
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 255
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        if 'default' not in kwargs:
            kwargs['default'] = self.default_field_class.DEFAULT
        super(Icon, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(Icon, self).formfield(**defaults)


class MiniText(django.db.models.TextField):
    default_field_class = fields.MiniText
    south_field_class = 'django.db.models.fields.TextField'

    def __init__(self, *args, **kwargs):
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        if 'default' not in kwargs:
            kwargs['default'] = ''
        super(MiniText, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(MiniText, self).formfield(**defaults)


class Responsive(MiniText):
    default_field_class = fields.Responsive

    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = ugettext('Responsive')
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        if 'default' not in kwargs:
            kwargs['default'] = ''
        super(Responsive, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(Responsive, self).formfield(**defaults)


class Size(django.db.models.CharField, SouthMixinBase):
    default_field_class = fields.Size
    south_field_class = 'django.db.models.fields.CharField'

    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = ugettext('Context')
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 255
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        if 'default' not in kwargs:
            kwargs['default'] = self.default_field_class.DEFAULT
        super(Size, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
            'choices_form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(Size, self).formfield(**defaults)

    def get_choices(self, **kwargs):
        # if there already is a "blank" choice, don't add another
        # default blank choice
        if '' in dict(self.choices).keys():
            kwargs['include_blank'] = False
        return super(Size, self).get_choices(**kwargs)


class IntegerField(django.db.models.IntegerField, SouthMixinBase):
    default_field_class = fields.Integer
    south_field_class = 'django.db.models.fields.IntegerField'

    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        django.db.models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
            'min_value': self.min_value,
            'max_value': self.max_value,
        }
        defaults.update(kwargs)
        return super(IntegerField, self).formfield(**defaults)


class ResponsivePrint(MiniText):
    default_field_class = fields.ResponsivePrint

    def __init__(self, *args, **kwargs):
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        if 'default' not in kwargs:
            kwargs['default'] = ''
        super(ResponsivePrint, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(ResponsivePrint, self).formfield(**defaults)


#TODO:
#   * btn-block, disabled
#   * pull-left, pull-right
#   * margins/padding
