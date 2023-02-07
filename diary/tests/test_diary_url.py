from django.test import SimpleTestCase
from django.urls import reverse, resolve

from diary.views import (
    MapView,
    CountryView,
)


class TestDiaryUrls(SimpleTestCase):

    def test_map_url_resolves(self):
        url = reverse('country-map')
        self.assertEquals(resolve(url).func.view_class, MapView)

    def test_country_page_url_resolves(self):
        url = reverse('country', args=[1])
        self.assertEquals(resolve(url).func.view_class,
                          CountryView)

