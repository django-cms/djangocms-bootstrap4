# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import django.forms.fields
from django.utils.translation import ugettext_lazy as _
from . import widgets
from .conf import settings


class Breakpoint(django.forms.fields.MultipleChoiceField):
    widget = widgets.Breakpoint
    CHOICES = (
        ('xs', _("Tiny (<{sm[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
        ('sm', _("Small (≥{sm[0]}px and <{md[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
        ('md', _("Medium (≥{md[0]}px and <{lg[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
        ('lg', _("Large (≥{lg[0]}px)".format(**settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS))),
    )
    INITIAL = ('lg', 'md', 'sm', 'xs',)

    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            kwargs['choices'] = self.CHOICES
        if 'initial' not in kwargs:
            kwargs['initial'] = self.INITIAL
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        super(Breakpoint, self).__init__(*args, **kwargs)


class ButtonType(django.forms.fields.ChoiceField):
    widget = widgets.ButtonType

    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            kwargs['choices'] = self.widget.renderer.BUTTON_TYPES.items()
        if 'initial' not in kwargs:
            kwargs['initial'] = self.widget.DEFAULT
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        super(ButtonType, self).__init__(*args, **kwargs)


class ButtonSize(django.forms.fields.ChoiceField):
    widget = widgets.ButtonSize

    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            kwargs['choices'] = self.widget.renderer.BUTTON_SIZES.items()
        if 'initial' not in kwargs:
            kwargs['initial'] = self.widget.DEFAULT
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        super(ButtonSize, self).__init__(*args, **kwargs)
