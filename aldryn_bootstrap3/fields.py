# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import django.forms.fields
from django.utils.translation import ugettext_lazy as _
from . import widgets, constants
from .conf import settings


# class Breakpoint(django.forms.fields.MultipleChoiceField):
#     widget = widgets.Breakpoint
#     CHOICES = (
#         ('xs', _("Tiny (<{sm[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
#         ('sm', _("Small (≥{sm[0]}px and <{md[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
#         ('md', _("Medium (≥{md[0]}px and <{lg[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
#         ('lg', _("Large (≥{lg[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
#     )
#     INITIAL = ('lg', 'md', 'sm', 'xs',)
#
#     def __init__(self, *args, **kwargs):
#         if 'choices' not in kwargs:
#             kwargs['choices'] = self.CHOICES
#         if 'initial' not in kwargs:
#             kwargs['initial'] = self.INITIAL
#         kwargs.pop('max_length', None)
#         kwargs.pop('widget', None)
#         super(Breakpoint, self).__init__(*args, **kwargs)


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
    # widget = widgets.Classes
    # DEFAULT = ''

    def __init__(self, *args, **kwargs):
        # if 'initial' not in kwargs:
        #     kwargs['initial'] = self.DEFAULT
        # kwargs.pop('max_length', None)
        # kwargs.pop('widget', None)
        # kwargs['widget'] = self.widget
        super(Classes, self).__init__(*args, **kwargs)
