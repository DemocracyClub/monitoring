import datetime

from django.test import TestCase

from url_store.models import URL

TODAY = datetime.datetime.today().date().isoformat()

class SmokeTests(TestCase):

    def test_base_date(self):
        url = URL(url="https://example.com/")
        self.assertEqual(url.base_date, TODAY)

    def test_base_file_name(self):
        url = URL(url="https://example.com/")
        self.assertEqual(
            url.base_file_name(),
            "{0}-example.com".format(TODAY)
        )

        url = URL(url="https://example.com/foo/bar/Baz")
        self.assertEqual(
            url.base_file_name(),
            "{0}-example.com-foo-bar-baz".format(TODAY)
        )

        url = URL(url="https://example.com/foo/bar/Baz?x=y")
        self.assertEqual(
            url.base_file_name(),
            "{0}-example.com-foo-bar-baz-x-y".format(TODAY)
        )

        url = URL(url="https://example.com/foo/bar/Baz?x=y&utm_content=buffer7f7f7&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer")
        self.assertEqual(
            url.base_file_name(),
            "{0}-example.com-foo-bar-baz-x-y".format(TODAY)
        )

