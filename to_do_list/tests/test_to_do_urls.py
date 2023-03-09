from django.test import SimpleTestCase
from django.urls import reverse, resolve

from to_do_list.views import (
    ToDoListView,
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



# urlpatterns = [
#     path('', ToDoListView.as_view(), name="to-do-list"),
#     path('to_do_lists/<int:pk>', ToDoListsView.as_view(), name="to-do-lists"), #pass country pk
#     path('to_do_lists/<int:pk>/delete', DeleteListView.as_view(), name="delete-list"), #pass ToDoList pk
#     path('to_do_lists/<int:pk>/edit', EditListView.as_view(), name="edit-list"), #pass ToDoList pk

#     path('to_do_items/<int:pk>', ToDoItemsView.as_view(), name="to-do-items"), #pass ToDoList pk
#     path('complete_item/<int:pk>', CompleteItemView.as_view(), name="complete-item"), #pass ToDoList pk
#     path('delete_item/<int:pk>', DeleteItemView.as_view(), name="delete-item"), #pass ToDoList pk
# ]