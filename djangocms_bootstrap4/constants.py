from django.conf import settings
from django.utils.translation import gettext_lazy as _


DEVICE_CHOICES = (
    ('xs', _('Extra small')),   # default <576px
    ('sm', _('Small')),         # default ≥576px
    ('md', _('Medium')),        # default ≥768px
    ('lg', _('Large')),         # default ≥992px
    ('xl', _('Extra large')),   # default ≥1200px
)
DEVICE_SIZES = tuple([size for size, name in DEVICE_CHOICES])

# Only adding block elements
TAG_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_TAG_CHOICES',
    ['div', 'section', 'article', 'header', 'footer', 'aside'],
)
TAG_CHOICES = tuple((entry, entry) for entry in TAG_CHOICES)

COLOR_STYLE_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_COLOR_STYLE_CHOICES',
    (
        ('primary', _('Primary')),
        ('secondary', _('Secondary')),
        ('success', _('Success')),
        ('danger', _('Danger')),
        ('warning', _('Warning')),
        ('info', _('Info')),
        ('light', _('Light')),
        ('dark', _('Dark')),
    )
)

ALIGN_CHOICES = (
    ('text-left', _('Left')),
    ('text-center', _('Center')),
    ('text-right', _('Right')),
)
