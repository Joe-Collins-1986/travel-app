from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import register


class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('home-register')
        self.assertEquals(resolve(url).func, register)

