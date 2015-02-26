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


class BootstrapMediaMixin(object):
    class Media:
        css = {
            'all': (
                '//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css',
                'https://static.dev.aldryn.net/cdn/bootstrap-iconpicker.min.css',
                '//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css',
            )
        }
        js = (
                'https://code.jquery.com/jquery-1.10.2.min.js',
                '//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js',
                'https://static.dev.aldryn.net/cdn/iconset/iconset-glyphicon.min.js',
                'https://static.dev.aldryn.net/cdn/iconset/iconset-fontawesome-4.2.0.min.js',
                'https://static.dev.aldryn.net/cdn/bootstrap-iconpicker.min.js',
        )


# class BreakpointsRenderer(django.forms.widgets.CheckboxFieldRenderer):
#     def render(self):
#         from django.template.loader import render_to_string
#         rendered = render_to_string(
#             'aldryn_bootstrap3/widgets/breakpoints.html',
#             {'selects': self},
#         )
#         return rendered
#
#
# class Breakpoints(BootstrapMediaMixin, django.forms.widgets.CheckboxSelectMultiple):
#     renderer = BreakpointsRenderer


class ContextRenderer(django.forms.widgets.RadioFieldRenderer):
    def render(self):
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'aldryn_bootstrap3/widgets/context.html',
            {'selects': self},
        )
        return rendered


class Context(BootstrapMediaMixin, django.forms.widgets.RadioSelect):
    renderer = ContextRenderer


class SizeRenderer(django.forms.widgets.RadioFieldRenderer):
    def render(self):
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'aldryn_bootstrap3/widgets/size.html',
            {'selects': self},
        )
        return rendered


class Size(django.forms.widgets.RadioSelect):
    renderer = SizeRenderer


class Icon(django.forms.widgets.TextInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super(Icon, self).render(name, value, attrs=attrs, **kwargs)
        if value is None:
            value = ''
        iconset = value.split('-')[0] if value and '-' in value else ''
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'aldryn_bootstrap3/widgets/icon.html',
            {
                'input_html': input_html,
                'value': value,
                'name': name,
                'iconset': iconset,
            },
        )
        return rendered
