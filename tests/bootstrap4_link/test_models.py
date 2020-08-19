from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_link.models import Bootstrap4Link


class B4LinkModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap4Link.objects.create()
        self.assertEqual(str(instance), "1")
