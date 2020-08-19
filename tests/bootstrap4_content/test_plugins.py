from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.contrib.bootstrap4_content.cms_plugins import (
    Bootstrap4BlockquotePlugin, Bootstrap4CodePlugin, Bootstrap4FigurePlugin,
)

from ..fixtures import B4TestFixture


class B4ContentPluginTestCase(B4TestFixture, CMSTestCase):

    def test_code_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CodePlugin.__name__,
            language=self.language,
            code_content="<p>hello world</p>",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "&lt;p&gt;hello world&lt;/p&gt;")

    def test_blockquote_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4BlockquotePlugin.__name__,
            language=self.language,
            quote_content="hello world",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<blockquote class="blockquote text-left">')

        # test quote_alignment
        add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4BlockquotePlugin.__name__,
            language=self.language,
            quote_content="hello world",
            quote_alignment="",
        )
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<blockquote class="blockquote">')

    def test_figure_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4FigurePlugin.__name__,
            language=self.language,
            figure_caption="hello world",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<figcaption class="figure-caption')
