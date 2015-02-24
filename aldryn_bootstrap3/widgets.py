# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import string
import itertools
from django.utils.translation import ugettext_lazy as _
import django.forms.widgets
from django.utils.datastructures import SortedDict
from django.utils.encoding import force_text
from django.utils.html import format_html, format_html_join

from .conf import settings


CONTEXT_CHOICES = (
    ('default', 'Default',),
    ('primary', 'Primary',),
    ('success', 'Success',),
    ('info', 'Info',),
    ('warning', 'Warning',),
    ('danger', 'Danger',),
)

SIZE_CHOICES = (
    ('lg', 'Large',),
    ('', 'Default',),
    ('sm', 'Small',),
    ('xs', 'Extra Small',),
)


class BootstrapMediaMixin(object):
    class Media:
        css = {
            'all': (
                '//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css',
                '//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css',
            )
        }


class BreakpointsRenderer(django.forms.widgets.CheckboxFieldRenderer):
    def render(self):
        return format_html(
            '<div class="form-row">{0}</div>',
            format_html_join(
                '',
                '<div class="field-box">'
                '<div class="container-thumbnail">'
                '<i style="font-size: 60px;" class="icon-{1}"></i>'
                '<div class="label">{0}</div>'
                '</div>'
                '</div>',
                (
                    (
                        force_text(w),
                        settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS[w.choice_value][1]
                    ) for w in self
                )
            )
        )


class Breakpoint(BootstrapMediaMixin, django.forms.widgets.CheckboxSelectMultiple):
    renderer = BreakpointsRenderer


class ButtonTypeRenderer(django.forms.widgets.RadioFieldRenderer):
    """
    Render sample buttons in different colors in the button's backend editor.
    """
    BUTTON_TYPES = SortedDict((
        ('btn-default', _('Default')),
        ('btn-primary', _('Primary')),
        ('btn-success', _('Success')),
        ('btn-info', _('Info')),
        ('btn-warning', _('Warning')),
        ('btn-danger', _('Danger')),
        ('btn-link', _('Link')),
    ))

    def render(self):
        return format_html(
            '<div class="form-row">{0}</div>',
            format_html_join(
                '\n',
                '<div class="field-box">'
                '<span class="btn {1}">{2}</span>'
                '<div class="label">{0}</div>'
                '</div>',
                (
                    (
                        force_text(w),
                        w.choice_value,
                        force_text(self.BUTTON_TYPES[w.choice_value])
                    ) for w in self
                )
            )
        )


class ButtonType(BootstrapMediaMixin, django.forms.widgets.RadioSelect):
    renderer = ButtonTypeRenderer
    DEFAULT = 'btn-default'


class ButtonSizeRenderer(django.forms.widgets.RadioFieldRenderer):
    """
    Render sample buttons in different sizes in the button's backend editor.
    """
    BUTTON_SIZES = SortedDict(
        (
            ('btn-lg', _('Large')),
            ('', _('Default')),
            ('btn-sm', _('Small')),
            ('btn-xs', _('Extra small')),
        )
    )

    def render(self):
        return format_html(
            '<div class="form-row">{0}</div>',
            format_html_join(
                '\n',
                '<div class="field-box"><div class="button-samples">'
                '<span class="btn btn-primary {1}">{2}</span>'
                '<span class="btn btn-default {1}">{2}</span>'
                '</div>'
                '<div class="label">{0}</div>'
                '</div>',
                (
                    (
                        force_text(w),
                        w.choice_value,
                        force_text(self.BUTTON_SIZES[w.choice_value])
                    ) for w in self
                )
            )
        )


class ButtonSize(django.forms.widgets.RadioSelect):
    renderer = ButtonSizeRenderer
    DEFAULT = ''
