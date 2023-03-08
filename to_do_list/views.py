from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
)
from diary.models import Country
from .models import ToDoList

# PLACEHOLDER
class ToDoList(View):

    def get(self, request):
        return render(
            request,
            "to_do_list/placeholder.html",
            {
            }
        )
# PLACEHOLDER

class ToDoLists(View):
    template_name = 'to_do_list/to_do_lists.html'

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)

        context = {}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        country = get_object_or_404(Country, pk=pk)

        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            todo = ToDoList.objects.create(
                title=title,
                description=description,
                user=request.user,
                country=country)
            
        return HttpResponseRedirect(reverse('to-do-lists', args=[pk]))



