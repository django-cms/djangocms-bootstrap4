# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# merges a list of classes with the attributes class key
def concat_classes(classes):
    store = ''
    for item in classes:
        if item:
            store += '{} '.format(item)
    return store
