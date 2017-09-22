# -*- coding: utf-8 -*-
from django.forms import models, IntegerField
from django.utils.translation import ugettext_lazy as _

from ...utils import IntegerRangeField

from .models import GRID_SIZE, Bootstrap4GridRow


class Bootstrap4GridRowForm(models.ModelForm):
    create = IntegerField(
        label=_('Create columns'),
        help_text=_('Number of columns to create when saving.'),
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )

    class Meta:
        pass
