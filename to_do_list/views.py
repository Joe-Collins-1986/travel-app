from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
)
from .models import ToDoList, ToDoItem
from diary.models import Country
from .forms import FullToDoListForm, ToDoItemForm

# PLACEHOLDER
class ToDoListView(View):

    def get(self, request):
        return render(
            request,
            "to_do_list/placeholder.html",
            {
            }
        )
# PLACEHOLDER

class ToDoListsView(View):
    template_name = 'to_do_list/to_do_lists.html'

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        lists = ToDoList.objects.filter(user=request.user, country=country, complete=False)

        add_list_form = FullToDoListForm()
        context = {
            'add_list_form': add_list_form,
            'lists': lists,
            'country': country
            }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        country = get_object_or_404(Country, pk=pk)
        add_list_form = FullToDoListForm(request.POST)

        if add_list_form.is_valid():
            todo = add_list_form.save(commit=False)
            todo.user = request.user
            todo.country = country
            todo.save()
            return HttpResponseRedirect(reverse('to-do-lists', args=[country.pk]))

        context = {'add_list_form': add_list_form}
        return render(request, self.template_name, context)


class ToDoItemsView(View):
    template_name = 'to_do_list/to_do_items.html'

    def get(self, request, pk):
        to_do_list = get_object_or_404(ToDoList, pk=pk)
        items = ToDoItem.objects.filter(list=to_do_list)

        add_item_form = ToDoItemForm()

        context = {
            'to_do_list': to_do_list,
            'items': items,
            'add_item_form': add_item_form
            }
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        to_do_list = get_object_or_404(ToDoList, pk=pk)
        items = ToDoItem.objects.filter(list=to_do_list)

        add_item_form = ToDoItemForm(request.POST)

        print(add_item_form.is_valid)
        if add_item_form.is_valid():
            item_add = add_item_form.save(commit=False)
            item_add.list = to_do_list
            item_add.save()

            url = reverse('to-do-items', args=[item_add.list.id])
            return redirect(url)

        context = {
            'to_do_list': to_do_list,
            'items': items,
            'add_item_form': add_item_form
            }
        return render(request, self.template_name, context)


class CompleteItemView(View):

    def get(self, request, pk):
        item = get_object_or_404(ToDoItem, pk=pk)
        item.complete = not item.complete
        item.save()

        url = reverse('to-do-items', args=[item.list.id])
        return redirect(url)


class DeleteItemView(View):

    def get(self, request, pk):
        item = get_object_or_404(ToDoItem, pk=pk)
        item.delete()

        url = reverse('to-do-items', args=[item.list.id])
        return redirect(url)



