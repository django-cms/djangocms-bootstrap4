# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import django.forms.fields
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from . import widgets, constants


class Context(django.forms.fields.ChoiceField):
    widget = widgets.Context
    CHOICES = constants.CONTEXT_CHOICES
    DEFAULT = constants.CONTEXT_DEFAULT

    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            kwargs['choices'] = self.CHOICES
        if 'initial' not in kwargs:
            kwargs['initial'] = self.DEFAULT
        kwargs.pop('coerce', None)
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        kwargs['widget'] = self.widget
        super(Context, self).__init__(*args, **kwargs)


class Size(django.forms.fields.ChoiceField):
    widget = widgets.Size
    CHOICES = constants.SIZE_CHOICES
    DEFAULT = 'md'

    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            kwargs['choices'] = self.CHOICES
        if 'initial' not in kwargs:
            kwargs['initial'] = self.DEFAULT
        kwargs.pop('coerce', None)
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        kwargs['widget'] = self.widget
        super(Size, self).__init__(*args, **kwargs)


class Icon(django.forms.fields.CharField):
    widget = widgets.Icon
    DEFAULT = ''

    def __init__(self, *args, **kwargs):
        if 'initial' not in kwargs:
            kwargs['initial'] = self.DEFAULT
        kwargs.pop('coerce', None)
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        kwargs['widget'] = self.widget
        super(Icon, self).__init__(*args, **kwargs)


class Integer(django.forms.fields.IntegerField):
    widget = django.forms.NumberInput

    def __init__(self, *args, **kwargs):
        kwargs.pop('coerce', None)
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        kwargs['widget'] = self.widget
        super(Integer, self).__init__(*args, **kwargs)


class Classes(django.forms.fields.CharField):
    widget = django.forms.widgets.Textarea


class MiniText(django.forms.fields.CharField):
    widget = widgets.MiniTextarea

    def __init__(self, *args, **kwargs):
        kwargs.pop('coerce', None)
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        kwargs['widget'] = self.widget
        super(MiniText, self).__init__(*args, **kwargs)


class LinkOrButton(django.forms.fields.ChoiceField):
    widget = widgets.LinkOrButton
    CHOICES = (
        ('lnk', 'link'),
        ('btn', 'button'),
    )
    DEFAULT = 'lnk'

    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            kwargs['choices'] = self.CHOICES
        if 'initial' not in kwargs:
            kwargs['initial'] = self.DEFAULT
        kwargs.pop('coerce', None)
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        kwargs['widget'] = self.widget
        super(LinkOrButton, self).__init__(*args, **kwargs)


class Responsive(MiniText):
    widget = widgets.Responsive


class ResponsivePrint(MiniText):
    widget = widgets.ResponsivePrint
