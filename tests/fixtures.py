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
        if hasattr(self.home, "publish"):
            self.home.publish(self.language)
        self.page = create_page(
            title="content",
            template="page.html",
            language=self.language,
        )
        if hasattr(self.page, "publish"):
            self.page.publish(self.language)
        else:
            self.page.publish = lambda *x, **y: None
        self.placeholder = self.page.get_placeholders("en").get(slot="content")
        self.superuser = self.get_superuser()
        self.request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        return super().setUp()

    def tearDown(self):
        self.page.delete()
        self.home.delete()
        self.superuser.delete()

        return super().tearDown()
