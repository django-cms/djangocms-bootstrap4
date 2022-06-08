from django.template.loader import select_template
from django.test import TestCase

from cms.api import add_plugin, create_page

from djangocms_bootstrap5.contrib.bootstrap5_carousel.cms_plugins import (
    Bootstrap5CarouselPlugin,
)
from djangocms_bootstrap5.contrib.bootstrap5_carousel.constants import (
    CAROUSEL_TEMPLATE_CHOICES,
)
from djangocms_bootstrap5.helpers import (
    concat_classes, get_plugin_template, get_template_path,
)


class B5HelpersTestCase(TestCase):

    def test_concat_classes(self):
        classes = ['class1 class2', 'class3']
        self.assertEqual(
            concat_classes(classes),
            'class1 class2 class3',
        )
        classes = []
        self.assertEqual(concat_classes(classes), '')

    def test_get_template_path(self):
        template = get_template_path(
            "carousel", "default", "slide"
        )
        result = "djangocms_bootstrap5/carousel/default/slide.html"
        self.assertEqual(template, result)
        status = select_template([template])
        self.assertEqual(status.template.name, result)

    def test_get_plugin_template(self):
        page = create_page(
            title="home",
            template="page.html",
            language="en",
        )
        instance = add_plugin(
            placeholder=page.placeholders.get(slot="content"),
            plugin_type=Bootstrap5CarouselPlugin.__name__,
            language="en",
        )
        template = get_plugin_template(
            instance, "carousel", "carousel",
            CAROUSEL_TEMPLATE_CHOICES,
        )
        self.assertEqual(template, "djangocms_bootstrap5/carousel/default/carousel.html")
        # trigger default template
        template = get_plugin_template(
            instance, "does_not", "exist",
            CAROUSEL_TEMPLATE_CHOICES,
        )
        self.assertEqual(template, "djangocms_bootstrap5/does_not/default/exist.html")
        # cleanup
        page.delete()
