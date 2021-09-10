from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap5.contrib.bootstrap5_media.cms_plugins import (
    Bootstrap5MediaBodyPlugin, Bootstrap5MediaPlugin,
)

from ..fixtures import B5TestFixture


class B5MediaPluginTestCase(B5TestFixture, CMSTestCase):

    def test_media_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5MediaPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="media">')

    def test_media_body_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5MediaBodyPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="media-body">')
