# -*- coding: utf-8 -*-


# merges a list of classes with the attributes class key
def concat_classes(classes):
    store = ''
    for item in classes:
        if item:
            store += '{} '.format(item)
    return store
