from django import forms

from djangocms_icon.fields import IconField
from djangocms_link.forms import LinkForm

from .constants import LINK_CHOICES
from .models import Bootstrap4Link


class Bootstrap4LinkForm(LinkForm):
    link_type = forms.ChoiceField(
        choices=LINK_CHOICES,
        initial=LINK_CHOICES[0][0],
        widget=forms.RadioSelect(attrs={'class': 'inline-block'}),
    )
    icon_left = IconField(required=False)
    icon_right = IconField(required=False)

    class Meta:
        model = Bootstrap4Link
        fields = '__all__'
