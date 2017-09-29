# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import models, IntegerField, BooleanField
from django.utils.translation import ugettext_lazy as _

from djangocms_bootstrap4.constants import DEVICE_SIZES
from djangocms_bootstrap4.fields import IntegerRangeField

from .constants import GRID_SIZE
from .models import Bootstrap4GridRow, Bootstrap4GridColumn


class Bootstrap4GridRowForm(models.ModelForm):
    create = IntegerField(
        label=_('Create columns'),
        help_text=_('Number of columns to create when saving.'),
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )

    class Meta:
        model = Bootstrap4GridRow
        fields = '__all__'


class Bootstrap4GridColumnBaseForm(models.ModelForm):
    class Meta:
        model = Bootstrap4GridColumn
        fields = '__all__'


# convert regular text type fields to number
extra_fields_column = {}
for size in DEVICE_SIZES:
    extra_fields_column['{}_col'.format(size)] = IntegerField(
        label='col-{}'.format(size),
        required=False,
        min_value=1,
        max_value=GRID_SIZE,
    )
    extra_fields_column['{}_order'.format(size)] = IntegerField(
        label='order-{}'.format(size),
        required=False,
        min_value=1,
        max_value=GRID_SIZE,
    )
    extra_fields_column['{}_ml'.format(size)] = BooleanField(
        label='ml-{}-auto'.format(size),
        required=False,
    )
    extra_fields_column['{}_mr'.format(size)] = BooleanField(
        label='mr-{}-auto'.format(size),
        required=False,
    )

Bootstrap4GridColumnForm = type(
    str('Bootstrap4GridColumnBaseForm'),
    (Bootstrap4GridColumnBaseForm,),
    extra_fields_column,
)
