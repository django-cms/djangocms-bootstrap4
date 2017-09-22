# -*- coding: utf-8 -*-


# merges a list of classes with the attributes class key
def concat_classes(classList, attributes):
    classes = ''
    for item in classList:
        if item:
            classes += '{} '.format(item)
    # check if "class" is define as attribute and merge
    if attributes.get('class'):
        classes += ' {}'.format(attributes.get('class', ''))
    return classes
