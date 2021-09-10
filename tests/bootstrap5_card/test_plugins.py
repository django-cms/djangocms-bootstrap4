from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap5.contrib.bootstrap5_card.cms_plugins import (
    Bootstrap5CardInnerPlugin, Bootstrap5CardPlugin,
)

from ..fixtures import B5TestFixture


class B5CardPluginTestCase(B5TestFixture, CMSTestCase):

    def test_card_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5CardPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="card">')

        # add card type
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5CardPlugin.__name__,
            language=self.language,
            card_type="card-columns",
            card_context="transparent",
            card_outline=True,
            card_alignment="text-right",
            card_text_color="white",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '<div class="card-columns border-transparent text-right text-white">',
        )

        # special case when card outline is given but not card context
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5CardPlugin.__name__,
            language=self.language,
            card_type="card-group",
            card_context="transparent",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="card-group bg-transparent">')

    def test_card_inner_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5CardInnerPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="card-body">')

        # add inner type
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5CardInnerPlugin.__name__,
            language=self.language,
            inner_type="card-footer",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="card-footer">')
