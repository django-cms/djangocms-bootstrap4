from django.forms.models import ModelForm
from django.forms.widgets import Textarea


class Bootstrap5CodeForm(ModelForm):
    class Meta:
        # When used inside djangocms-text-ckeditor
        # this causes the label field to be prefilled with the selected text.
        widgets = {
            'code_content': Textarea(attrs={'class': 'js-ckeditor-use-selected-text'}),
        }
