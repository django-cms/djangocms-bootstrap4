from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.constants import COLOR_STYLE_CHOICES
from djangocms_bootstrap4.fields import AttributesField


class Bootstrap4Badge(CMSPlugin):
    """
    Components > "Badge" Plugin
    https://getbootstrap.com/docs/4.0/components/badge/
    """
    badge_text = models.CharField(
        verbose_name=_('Badge text'),
        max_length=255,
    )
    badge_context = models.CharField(
        verbose_name=_('Context'),
        choices=COLOR_STYLE_CHOICES,
        default=COLOR_STYLE_CHOICES[0][0],
        max_length=255,
    )
    badge_pills = models.BooleanField(
        verbose_name=_('Pills style'),
        default=False,
        help_text=_('Activates the pills style.'),
    )

    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return f'({self.badge_context})'
