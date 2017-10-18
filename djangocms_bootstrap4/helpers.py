# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import six
from django.utils.safestring import mark_safe
from django.utils.functional import lazy


def concat_classes(classes):
    """
    merges a list of classes and return concatinated string
    """
    return ' '.join(_class for _class in classes if _class)


# use mark_safe_lazy to delay the translation when using mark_safe
# otherwise they will not be added to /locale/
# https://docs.djangoproject.com/en/1.11/topics/i18n/translation/#other-uses-of-lazy-in-delayed-translations
mark_safe_lazy = lazy(mark_safe, six.text_type)
