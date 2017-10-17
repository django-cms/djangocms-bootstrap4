# -*- coding: utf-8 -*-
from django.test import TestCase

from djangocms_bootstrap4.helpers import (
    concat_classes,
)


class GridInstanceTestCase(TestCase):

    def test_concat_classes(self):
        classes = concat_classes(['class1 class2', 'class3'])
        self.assertEqual(classes, 'class1 class2 class3')
