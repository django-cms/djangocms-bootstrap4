# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django import forms
from django.utils.translation import ugettext_lazy as _

from . import models, constants


class RowPluginBaseForm(forms.ModelForm):
    create = forms.IntegerField(
        label=_('Create Columns'),
        help_text=_('Create this number of columns inside'),
        required=False,
        min_value=0,
    )

    class Meta:
        model = models.Bootstrap3RowPlugin
        # fields = ('classes',)
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


extra_fields = {}
for size, name in constants.DEVICE_CHOICES:
    extra_fields["create_{}_size".format(size)] = forms.IntegerField(
        label=_('Column size ({})'.format(name)),
        help_text=('Width of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields["create_{}_offset".format(size)] = forms.IntegerField(
        label=_('Offset size ({})'.format(name)),
        help_text=('Offset of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )


RowPluginForm = type(str('RowPluginBaseForm'), (RowPluginBaseForm,), extra_fields)
