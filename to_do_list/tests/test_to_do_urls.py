from django.test import SimpleTestCase
from django.urls import reverse, resolve

from to_do_list.views import (
    ToDoListsView,
    DeleteListView,
    EditListView,
    ToDoItemsView,
    CompleteItemView,
    DeleteItemView,
)


class TestToDoUrls(SimpleTestCase):

    def test_lists_view_url_resolves(self):
        url = reverse('to-do-lists', args=[1])
        self.assertEquals(resolve(url).func.view_class, ToDoListsView)

    def test_lists_delete_url_resolves(self):
        url = reverse('delete-list', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteListView)

    def test_lists_edit_url_resolves(self):
        url = reverse('edit-list', args=[1])
        self.assertEquals(resolve(url).func.view_class, EditListView)

    def test_items_view_url_resolves(self):
        url = reverse('to-do-items', args=[1])
        self.assertEquals(resolve(url).func.view_class, ToDoItemsView)

    def test_items_complete_url_resolves(self):
        url = reverse('complete-item', args=[1])
        self.assertEquals(resolve(url).func.view_class, CompleteItemView)

    def test_items_delete_url_resolves(self):
        url = reverse('delete-item', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteItemView)
