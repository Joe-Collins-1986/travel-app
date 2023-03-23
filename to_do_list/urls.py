from django.urls import path
from .views import (
    AddListView,
    DeleteListView,
    EditListView,
    ToDoItemsView,
    CompleteItemView,
    DeleteItemView,

)

urlpatterns = [
    path(
        'to_do_list/<int:pk>/add',
        AddListView.as_view(),
        name="add-list"),
    path(
        'to_do_lists/<int:pk>/delete',
        DeleteListView.as_view(),
        name="delete-list"),
    path(
        'to_do_lists/<int:pk>/edit',
        EditListView.as_view(),
        name="edit-list"),
    path(
        'to_do_items/<int:pk>',
        ToDoItemsView.as_view(),
        name="to-do-items"),
    path(
        'complete_item/<int:pk>',
        CompleteItemView.as_view(),
        name="complete-item"),
    path(
        'delete_item/<int:pk>',
        DeleteItemView.as_view(),
        name="delete-item"),
]
