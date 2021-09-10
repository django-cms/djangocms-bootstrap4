from django.test import TestCase

from djangocms_bootstrap5.contrib.bootstrap5_utilities.models import (
    Bootstrap5Spacing,
)


class B5UtilitiesModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap5Spacing.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(.m-0)")

        instance.space_device = "md"
        self.assertEqual(instance.get_short_description(), "(.m-md-0)")
