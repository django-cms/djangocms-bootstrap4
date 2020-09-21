from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_picture.models import AbstractPicture


class Bootstrap4Picture(AbstractPicture):
    """
    Content > "Image" Plugin
    https://getbootstrap.com/docs/4.0/content/images/
    """
    picture_fluid = models.BooleanField(
        verbose_name=_('Responsive'),
        default=True,
        help_text=_('Adds the .img-fluid class to make the image responsive.'),
    )
    picture_rounded = models.BooleanField(
        verbose_name=_('Rounded'),
        default=False,
        help_text=_('Adds the .rounded class for round corners.'),
    )
    picture_thumbnail = models.BooleanField(
        verbose_name=_('Thumbnail'),
        default=False,
        help_text=_('Adds the .img-thumbnail class.'),
    )
    picture_customclasses = models.CharField(
        verbose_name=('Custom'),
        default="",
        help_text=_('Adds the extra space separated classes.'),
        blank=True,
        max_length=255
    )


    class Meta:
        abstract = False

    def __str__(self):
        return str(self.pk)
