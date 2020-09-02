from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.contrib.bootstrap4_listgroup.cms_plugins import (
    Bootstrap4ListGroupItemPlugin, Bootstrap4ListGroupPlugin,
)

from ..fixtures import B4TestFixture


class B4ListGroupPluginTestCase(B4TestFixture, CMSTestCase):

    def test_list_group_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4ListGroupPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="list-group">')

        # test list_group_flush option
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4ListGroupPlugin.__name__,
            language=self.language,
            list_group_flush=True,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="list-group list-group-flush">')

    def test_list_group_item_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4ListGroupItemPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="list-group-item">')

        # test list_context and list_state options
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4ListGroupItemPlugin.__name__,
            language=self.language,
            list_context="primary",
            list_state="active",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="list-group-item list-group-item-primary active">')
