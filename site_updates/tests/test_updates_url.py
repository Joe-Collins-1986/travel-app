from django.test import SimpleTestCase
from django.urls import reverse, resolve

from site_updates.views import (
    AdminUpdatesListView,
    AdminDetailUpdateView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)


class TestSiteUpdatesUrls(SimpleTestCase):

    def test_admin_updates_url_resolves(self):
        url = reverse('all-admin-updates')
        self.assertEquals(resolve(url).func.view_class, AdminUpdatesListView)

    def test_admin_updates_detail_url_resolves(self):
        url = reverse('admin-update-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, AdminDetailUpdateView)

    def test_comment_create_view_url_resolves(self):
        url = reverse('comment-create', args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentCreateView)

    def test_comment_update_view_url_resolves(self):
        url = reverse('comment-update', args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentUpdateView)

    def test_comment_delete_view_url_resolves(self):
        url = reverse('comment-delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentDeleteView)



