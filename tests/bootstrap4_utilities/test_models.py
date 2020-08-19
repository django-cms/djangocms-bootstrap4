from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_utilities.models import (
    Bootstrap4Spacing,
)


class B4UtilitiesModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap4Spacing.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(.m-0)")

        instance.space_device = "md"
        self.assertEqual(instance.get_short_description(), "(.m-md-0)")
