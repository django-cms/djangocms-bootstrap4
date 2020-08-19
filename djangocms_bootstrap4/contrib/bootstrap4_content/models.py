from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.constants import ALIGN_CHOICES
from djangocms_bootstrap4.fields import AttributesField

from .constants import CODE_TYPE_CHOICES


class Bootstrap4Code(CMSPlugin):
    """
    Content > "Code" Plugin
    https://getbootstrap.com/docs/4.0/content/code/
    """
    code_content = models.TextField(
        verbose_name=_('Code'),
    )
    tag_type = models.CharField(
        verbose_name=_('Code type'),
        choices=CODE_TYPE_CHOICES,
        default=CODE_TYPE_CHOICES[0][0],
        max_length=255,
    )
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '<{}>'.format(self.tag_type)


class Bootstrap4Blockquote(CMSPlugin):
    """
    Content > "Blockquote" Plugin
    https://getbootstrap.com/docs/4.0/content/typography/#blockquotes
    """
    quote_content = models.TextField(
        verbose_name=_('Quote'),
    )
    quote_origin = models.TextField(
        verbose_name=_('Cite'),
        blank=True,
    )
    quote_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=ALIGN_CHOICES,
        default=ALIGN_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return self.quote_content


class Bootstrap4Figure(CMSPlugin):
    """
    Content > "Figure" Plugin
    https://getbootstrap.com/docs/4.0/content/figures/
    """
    figure_caption = models.CharField(
        verbose_name=_('Caption'),
        max_length=255,
    )
    figure_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=ALIGN_CHOICES,
        default=ALIGN_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return self.figure_caption
