from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_picture.models import (
    Bootstrap4Picture,
)


class B4PictureModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap4Picture.objects.create()
        self.assertEqual(str(instance), "1")
