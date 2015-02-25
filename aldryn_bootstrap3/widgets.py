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
                '//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css',
                '//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css',
            )
        }


class BreakpointsRenderer(django.forms.widgets.CheckboxFieldRenderer):
    def render(self):
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'aldryn_bootstrap3/widgets/breakpoints.html',
            {'selects': self},
        )
        return rendered


class Breakpoints(BootstrapMediaMixin, django.forms.widgets.CheckboxSelectMultiple):
    renderer = BreakpointsRenderer


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
