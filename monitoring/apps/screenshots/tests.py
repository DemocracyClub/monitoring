from django.test import TestCase

from .models import Screenshot
from url_store.models import URL

from screenshots.utils import WebPageScreenshot

class TestSCreenShot(TestCase):
    # def test_single_page(self):
    #     s = WebPageScreenshot()
    #     x = s.capture('https://democracyclub.org.uk/')
    #     with open('/tmp/xxx.png', 'wb') as foo:
    #         foo.write(x.getvalue())

    def test_model(self):
        url = URL(url='https://www.gov.uk')
        url.save()
        m = Screenshot(url=url)
        m.save()
        m.take_screenshot()

        url = URL(url='https://democracyclub.org.uk/')
        url.save()
        m = Screenshot(url=url)
        m.save()
        m.take_screenshot()

