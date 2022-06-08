from django.test import TestCase

from djangocms_bootstrap5.contrib.bootstrap5_carousel.models import (
    Bootstrap5Carousel, Bootstrap5CarouselSlide,
)

from ..helpers import get_filer_image


class B5CarouselModelTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.image = get_filer_image()

    def tearDown(self):
        super().tearDown()
        self.image.delete()

    def test_carousel_instance(self):
        instance = Bootstrap5Carousel.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(
            instance.get_short_description(),
            "(default) Interval: 5000, Controls: True, Indicators: True, "
            "Keyboard: True, Pause: hover, Ride: carouselWrap: True",
        )

    def test_carousel_slide_instance(self):
        instance = Bootstrap5CarouselSlide.objects.create()
        instance.clean()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
        # test carousel content strings
        instance.carousel_image = self.image
        instance.carousel_content = "hello world"
        self.assertEqual(
            instance.get_short_description(),
            "test_file.jpg (hello world)",
        )
        instance.carousel_content = "hello world" + "#" * 100
        self.assertEqual(
            instance.get_short_description(),
            "test_file.jpg (hello world" + "#" * 89 + "...)",
        )
        self.assertEqual(instance.get_link(), "")
        # test image ouput options
        instance.carousel_content = None
        instance.carousel_image = get_filer_image(name="image")
        self.assertEqual(instance.get_short_description(), "image")
        instance.carousel_image = get_filer_image(original_filename=False)
        self.assertEqual(instance.get_short_description(), "Image")
