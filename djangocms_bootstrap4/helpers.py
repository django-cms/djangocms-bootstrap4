# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def concat_classes(classes):
    """
    merges a list of classes and return concatinated string
    """
    return ' '.join(_class for _class in classes if _class)
