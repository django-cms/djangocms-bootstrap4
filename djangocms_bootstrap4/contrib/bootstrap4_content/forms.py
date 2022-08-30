from django.conf import settings as django_settings
from django.forms.models import ModelForm
from django.forms.widgets import Textarea


class Bootstrap4CodeForm(ModelForm):
    class Media:
        js = (
            "admin/vendor/ace/ace.js"
            if "djangocms_static_ace" in django_settings.INSTALLED_APPS
            else "https://cdnjs.cloudflare.com/ajax/libs/ace/1.9.6/ace.js",
        )

    class Meta:
        # When used inside djangocms-text-ckeditor
        # this causes the label field to be prefilled with the selected text.
        widgets = {
            'code_content': Textarea(attrs={'class': 'js-ckeditor-use-selected-text'}),
        }
