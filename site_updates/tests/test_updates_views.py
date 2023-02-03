from django.test import TestCase
from django.urls import reverse


class TestAdminUpdatesListView(TestCase):
    """ Test Admin Updates Function """

    def test_admin_updates_list_get(self):
        """ Test loading of admin updates page """
        response = self.client.get(reverse('all-admin-updates'))
        self.assertEqual(response.status_code, 200)