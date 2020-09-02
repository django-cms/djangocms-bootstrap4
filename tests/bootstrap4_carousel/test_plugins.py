from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.contrib.bootstrap4_carousel.cms_plugins import (
    Bootstrap4CarouselPlugin, Bootstrap4CarouselSlidePlugin,
)

from ..fixtures import B4TestFixture
from ..helpers import get_filer_image


class B4CarouselPluginTestCase(B4TestFixture, CMSTestCase):

    def setUp(self):
        super().setUp()
        self.image = get_filer_image()

    def tearDown(self):
        super().tearDown()
        self.image.delete()

    def test_carousel_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CarouselPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="carousel slide"')
        self.assertContains(response, 'data-interval="5000"')
        self.assertContains(response, 'data-keyboard="true"')
        self.assertContains(response, 'data-pause="hover"')
        self.assertContains(response, 'data-ride="carousel"')
        self.assertContains(response, 'data-wrap="true"')

    def test_carousel_slide_plugin(self):
        row = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CarouselPlugin.__name__,
            language=self.language,
        )
        plugin = add_plugin(
            target=row,
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CarouselSlidePlugin.__name__,
            language=self.language,
            carousel_image=self.image,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="carousel slide"')

        # testing aspect ratio variant
        # also testing multiply entries
        row = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CarouselPlugin.__name__,
            language=self.language,
            carousel_aspect_ratio="16x9",
        )
        add_plugin(
            target=row,
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CarouselSlidePlugin.__name__,
            language=self.language,
            carousel_image=self.image,
        )
        add_plugin(
            target=row,
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CarouselSlidePlugin.__name__,
            language=self.language,
            carousel_image=self.image,
        )
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="carousel slide"')
