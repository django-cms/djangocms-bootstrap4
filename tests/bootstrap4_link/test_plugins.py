from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.contrib.bootstrap4_link.cms_plugins import (
    Bootstrap4LinkPlugin,
)

from ..fixtures import B4TestFixture


class B4LinkPluginTestCase(B4TestFixture, CMSTestCase):

    def test_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4LinkPlugin.__name__,
            language=self.language,
            external_link="https://www.divio.com",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="https://www.divio.com"')

        # add more options
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4LinkPlugin.__name__,
            language=self.language,
            external_link="https://www.divio.com",
            link_context="primary",
            link_size="btn-sm",
            link_block=True,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="text-primary btn-sm btn-block"')

        # alternate version for link_type
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4LinkPlugin.__name__,
            language=self.language,
            external_link="https://www.divio.com",
            link_context="primary",
            link_type="btn",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="btn btn-primary"')

        # alternate version using link_outline
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4LinkPlugin.__name__,
            language=self.language,
            external_link="https://www.divio.com",
            link_context="primary",
            link_type="btn",
            link_outline=True,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="btn btn-outline-primary"')
