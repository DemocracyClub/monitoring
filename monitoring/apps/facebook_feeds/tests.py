from django.test import TestCase

from .models import FacebookAccount


class TestFaceook(TestCase):

    def test_get_posts(self):
        FacebookAccount(username='nhacambpeckham').get_posts()