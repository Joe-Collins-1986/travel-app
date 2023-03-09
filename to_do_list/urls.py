from django.urls import path
from .views import (
    ToDoListView,
    ToDoListsView,
    DeleteListView,
    EditListView,
    ToDoItemsView,
    CompleteItemView,
    DeleteItemView,

)

urlpatterns = [
    path('', ToDoListView.as_view(), name="to-do-list"),
    path('to_do_lists/<int:pk>', ToDoListsView.as_view(), name="to-do-lists"), #pass country pk
    path('to_do_lists/<int:pk>/delete', DeleteListView.as_view(), name="delete-list"), #pass ToDoList pk
    path('to_do_lists/<int:pk>/edit', EditListView.as_view(), name="edit-list"), #pass ToDoList pk

    path('to_do_items/<int:pk>', ToDoItemsView.as_view(), name="to-do-items"), #pass ToDoList pk
    path('complete_item/<int:pk>', CompleteItemView.as_view(), name="complete-item"), #pass ToDoList pk
    path('delete_item/<int:pk>', DeleteItemView.as_view(), name="delete-item"), #pass ToDoList pk
]