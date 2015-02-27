# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import django.forms.fields
from django.utils.translation import ugettext_lazy as _
from . import widgets, constants
from .conf import settings


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


# class Breakpoints(django.forms.fields.MultipleChoiceField):
#     widget = widgets.Breakpoints
#     CHOICES = constants.BREAKPOINTS_CHOICES
#     DEFAULT = constants.BREAKPOINTS_DEFAULT
#
#     def __init__(self, *args, **kwargs):
#         if 'choices' not in kwargs:
#             kwargs['choices'] = self.CHOICES
#         if 'initial' not in kwargs:
#             kwargs['initial'] = self.DEFAULT
#         kwargs.pop('coerce', None)
#         kwargs.pop('max_length', None)
#         kwargs.pop('widget', None)
#         kwargs['widget'] = self.widget
#         super(Breakpoints, self).__init__(*args, **kwargs)


class Size(django.forms.fields.ChoiceField):
    widget = widgets.Size
    CHOICES = constants.SIZE_CHOICES
    DEFAULT = constants.SIZE_DEFAULT

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


class Classes(django.forms.fields.CharField):
    pass


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
