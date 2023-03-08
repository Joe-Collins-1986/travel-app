from django.urls import path
from .views import (
    ToDoList,
    ToDoLists,
)

urlpatterns = [
    path('', ToDoList.as_view(), name="to-do-list"),
    path('to_do_lists/<int:pk>', ToDoLists.as_view(), name="to-do-lists"), #pass country pk
]