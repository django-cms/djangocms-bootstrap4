# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.forms import forms
from . import fields


class Frm(forms.Form):
    breakpoints = fields.Breakpoint()
