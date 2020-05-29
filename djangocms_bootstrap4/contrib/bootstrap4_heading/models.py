from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from enumfields import EnumField
from slugify import slugify

from djangocms_bootstrap4.contrib.bootstrap4_heading.constants import HEADING_ALIGNMENT_ENUM
from djangocms_bootstrap4.contrib.bootstrap4_heading.constants import HEADING_COLOR_ENUM
from djangocms_bootstrap4.contrib.bootstrap4_heading.constants import HEADING_SIZE_UNIT_ENUM
from djangocms_bootstrap4.contrib.bootstrap4_heading.constants import HEADING_TAG_ENUM
from djangocms_bootstrap4.contrib.bootstrap4_heading.constants import HEADING_TYPE_ENUM
from djangocms_bootstrap4.fields import AttributesField


class Bootstrap4Heading(CMSPlugin):
    # this name isn't self-explanatory because djangocms-text-ckeditor#528
    name = models.TextField(max_length=2048, verbose_name=_("Text"))

    tag = EnumField(
        HEADING_TAG_ENUM, default=HEADING_TAG_ENUM.H1, max_length=32,
    )
    alignment = EnumField(
        HEADING_ALIGNMENT_ENUM, default=HEADING_ALIGNMENT_ENUM.LEFT, max_length=32,
    )

    size = models.FloatField(blank=True, null=True, help_text=_("Optional"))
    size_unit = EnumField(
        HEADING_SIZE_UNIT_ENUM, default=HEADING_SIZE_UNIT_ENUM.PX, max_length=32,
    )

    type = EnumField(
        HEADING_TYPE_ENUM,
        default=HEADING_TYPE_ENUM.NORMAL,
        max_length=32,
        blank=True, null=True,
    )
    color = EnumField(
        HEADING_COLOR_ENUM, default=HEADING_COLOR_ENUM.DARK, max_length=32,
    )

    attributes = AttributesField()

    def get_anchor(self) -> str:
        return slugify(self.name)

    def __str__(self) -> str:
        if self.name:
            return self.name
        return ""
