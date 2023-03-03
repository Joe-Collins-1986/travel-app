from django.test import SimpleTestCase
from django.urls import reverse, resolve

from diary.views import (
    MapView,
    CountryView,
    DiaryAllPostsView,
    DiaryTagsView,
    DiaryCreateView,
    DiaryUpdateView,
    DiaryDeleteView,
)


class TestDiaryUrls(SimpleTestCase):

    def test_map_url_resolves(self):
        url = reverse('country-map')
        self.assertEquals(resolve(url).func.view_class, MapView)

    def test_country_page_url_resolves(self):
        url = reverse('country', args=[1])
        self.assertEquals(resolve(url).func.view_class,
                          CountryView)

    def test_diary_all_posts_url_resolves(self):
        url = reverse('diary-all-posts', args=[1])
        self.assertEquals(resolve(url).func.view_class,
                          DiaryAllPostsView)

    def test_diary_tags_page_url_resolves(self):
        url = reverse('diary-tags', args=[1])
        self.assertEquals(resolve(url).func.view_class,
                          DiaryTagsView)

    def test_diary_create_url_resolves(self):
        url = reverse('diary-create', args=[1])
        self.assertEquals(resolve(url).func.view_class,
                          DiaryCreateView)

    def test_diary_update_url_resolves(self):
        url = reverse('diary-update', args=[1])
        self.assertEquals(resolve(url).func.view_class,
                          DiaryUpdateView)

    def test_diary_delete_url_resolves(self):
        url = reverse('diary-delete', args=[1])
        self.assertEquals(resolve(url).func.view_class,
                          DiaryDeleteView)

