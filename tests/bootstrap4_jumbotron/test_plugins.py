from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.contrib.bootstrap4_jumbotron.cms_plugins import (
    Bootstrap4JumbotronPlugin,
)

from ..fixtures import B4TestFixture


class B4JumbotronPluginTestCase(B4TestFixture, CMSTestCase):

    def test_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4JumbotronPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="jumbotron">')

        # fluid option
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4JumbotronPlugin.__name__,
            language=self.language,
            fluid=True,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="jumbotron jumbotron-fluid">')
