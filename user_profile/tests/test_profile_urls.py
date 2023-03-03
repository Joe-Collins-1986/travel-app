from django.test import SimpleTestCase
from django.urls import reverse, resolve

from user_profile.views import (
    ProfilePageView,
    UpdateProfilePageView,
)


class TestProfileUrls(SimpleTestCase):

    def test_profile_page_url_resolves(self):
        url = reverse('profile-page')
        self.assertEquals(resolve(url).func.view_class, ProfilePageView)

    def test_update_profile_page_url_resolves(self):
        url = reverse('update-profile-page')
        self.assertEquals(resolve(url).func.view_class,
                          UpdateProfilePageView)


