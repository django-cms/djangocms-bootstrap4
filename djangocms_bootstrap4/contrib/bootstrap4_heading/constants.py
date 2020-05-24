from django.conf import settings
from enumfields import Enum
from django.utils.translation import ugettext_lazy as _


class SizeUnit(Enum):
    PX = 'px'
    REM = 'rem'
    EM = 'em'

    class Labels:
        PX = _('Pixels')
        REM = _('Font size of the root element (rem)')
        EM = _('Font size of the parent (em)')


class HeadingTag(Enum):
    H1 = 'h1'
    H2 = 'h2'
    H3 = 'h3'
    H4 = 'h4'
    H5 = 'h5'
    H6 = 'h6'
    DIV = 'div'
    P = 'p'


class HeadingColor(Enum):
    DARK = 'dark'
    WHITE = 'white'


class HeadingAlignment(Enum):
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'


class HeadingType(Enum):
    NORMAL = 'normal'


HEADING_SIZE_UNIT_ENUM = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_HEADING_SIZE_UNIT_ENUM',
    SizeUnit,
)
HEADING_TAG_ENUM = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_HEADING_TAG_ENUM',
    HeadingTag,
)
HEADING_COLOR_ENUM = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_HEADING_COLOR_ENUM',
    HeadingColor,
)
HEADING_ALIGNMENT_ENUM = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_HEADING_ALIGNMENT_ENUM',
    HeadingAlignment,
)
HEADING_TYPE_ENUM = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_HEADING_TYPE_ENUM',
    HeadingType,
)
