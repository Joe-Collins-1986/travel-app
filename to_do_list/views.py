from django.shortcuts import render
from django.views.generic import (
    View,
)

class ToDoList(View):

    def get(self, request):
        return render(
            request,
            "to_do_list/placeholder.html",
            {
            }
        )
