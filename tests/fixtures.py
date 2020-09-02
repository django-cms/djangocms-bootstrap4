from cms.api import create_page


class B4TestFixture:
    """Sets up generic setUp and tearDown methods for tests."""

    def setUp(self):
        self.language = "en"
        self.home = create_page(
            title="home",
            template="page.html",
            language=self.language,
        )
        self.home.publish(self.language)
        self.page = create_page(
            title="content",
            template="page.html",
            language=self.language,
        )
        self.page.publish(self.language)
        self.placeholder = self.page.placeholders.get(slot="content")
        self.superuser = self.get_superuser()
        self.request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        return super().setUp()

    def tearDown(self):
        self.page.delete()
        self.home.delete()
        self.superuser.delete()

        return super().tearDown()
