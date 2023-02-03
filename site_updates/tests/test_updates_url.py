from django.test import SimpleTestCase
from django.urls import reverse, resolve

from site_updates.views import (
    AdminUpdatesListView
)


class TestSiteUpdatesUrls(SimpleTestCase):

    def test_admin_updates_url_resolves(self):
        url = reverse('all-admin-updates')
        self.assertEquals(resolve(url).func.view_class, AdminUpdatesListView)