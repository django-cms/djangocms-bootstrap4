from django.test import TestCase

from djangocms_bootstrap5.contrib.bootstrap5_jumbotron.models import (
    Bootstrap5Jumbotron,
)


class B5JumbotronModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap5Jumbotron.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
        instance.fluid = True
        self.assertEqual(instance.get_short_description(), "(Fluid)")
