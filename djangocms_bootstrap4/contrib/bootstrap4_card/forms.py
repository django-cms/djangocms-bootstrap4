# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import models, ChoiceField
from django.utils.translation import ugettext_lazy as _

from djangocms_bootstrap4.constants import DEVICE_SIZES
from djangocms_bootstrap4.fields import IntegerRangeField

from .constants import CARD_BLUEPRINTS
from .models import Bootstrap4Card


class Bootstrap4CardForm(models.ModelForm):
    # TODO maybe add number of cards to generate
    blueprint = ChoiceField(
        label=_('Choose blueprint'),
        choices=CARD_BLUEPRINTS,
        required=False,
    )

    class Meta:
        model = Bootstrap4Card
        fields = '__all__'
