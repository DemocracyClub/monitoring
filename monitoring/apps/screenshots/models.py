import base64

from django.db import models
from django.core.files.base import ContentFile
from django.conf import settings

import requests

from url_store.models import URL

def download_file_name(instance, filename):
    return "/".join([
        "screenshots",
        instance.url.base_file_name()
    ]) + '.png'


class Screenshot(models.Model):
    url = models.ForeignKey(URL)
    image = models.ImageField(upload_to=download_file_name)

    def take_screenshot(self):
        url = requests.get(self.url.url).url
        br = settings.WEBDRIVER()
        br.get(self.url.url)
        ss =  br.get_screenshot_as_base64()
        # import ipdb; ipdb.set_trace()
        # ss = br.save_screenshot('screenshot.png')
        br.quit()
        self.image.save(self.url.base_file_name(), ContentFile(base64.decodestring(ss)))
