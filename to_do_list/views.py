from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import (
    View,
)
from .models import ToDoList, ToDoItem
from diary.models import Country
from .forms import FullToDoListForm, ToDoItemForm

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class AddListView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    template_name = 'to_do_list/to_do_list_add.html'

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        lists = ToDoList.objects.filter(user=request.user, country=country)

        list_form = FullToDoListForm()
        context = {
            'list_form': list_form,
            'country': country,
            "tab_title": "Add List"
            }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        country = get_object_or_404(Country, pk=pk)
        list_form = FullToDoListForm(request.POST)

        # valid form actions
        if list_form.is_valid():
            todo = list_form.save(commit=False)
            todo.user = request.user
            todo.country = country
            todo.save()
            messages.success(
                self.request,
                'YOUR NEW TO-DO LIST HAS BEEN CREATED SUCCESSFULLY'
                )
            url = reverse('country', args=[country.pk])
            return redirect(
                f'{url}#to_do_list_location'
                )


class DeleteListView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        list = get_object_or_404(ToDoList, pk=pk)
        list.delete()

        url = reverse('country', args=[list.country.pk])
        messages.success(
            self.request,
            'YOUR TO-DO LIST HAS BEEN DELETED SUCCESSFULLY'
            )
        return redirect(
                f'{url}#to_do_list_location'
                )

    # validate request user is author and restrict if not
    def test_func(self):
        list = get_object_or_404(ToDoList, pk=self.kwargs['pk'])
        return self.request.user == list.user


class EditListView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    template_name = 'to_do_list/to_do_list_update.html'

    def get(self, request, pk):
        list = get_object_or_404(ToDoList, pk=pk)

        list_form = FullToDoListForm(instance=list)

        context = {
            'list_form': list_form,
            'list': list,
            "tab_title": "Edit List"
            }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        list = get_object_or_404(ToDoList, pk=pk)

        list_form = FullToDoListForm(request.POST, instance=list)

        # form valid actions
        if list_form.is_valid():
            edit = list_form.save(commit=False)
            edit.save()

            url = reverse('country', args=[edit.country.pk])
            messages.success(
                self.request,
                f'YOUR TO-DO LIST HAS BEEN UPDATED SUCCESSFULLY'
                )
            return redirect(
                f'{url}#to_do_list_location'
                )

    # validate request user is author and restrict if not
    def test_func(self):
        list = get_object_or_404(ToDoList, pk=self.kwargs['pk'])
        return self.request.user == list.user


class ToDoItemsView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    template_name = 'to_do_list/to_do_items.html'

    def get(self, request, pk):
        to_do_list = get_object_or_404(ToDoList, pk=pk)
        items = ToDoItem.objects.filter(list=to_do_list)

        add_item_form = ToDoItemForm()

        context = {
            'to_do_list': to_do_list,
            'items': items,
            'add_item_form': add_item_form,
            "tab_title": "Task Items"
            }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        to_do_list = get_object_or_404(ToDoList, pk=pk)
        items = ToDoItem.objects.filter(list=to_do_list)

        add_item_form = ToDoItemForm(request.POST)

        # form valid actions
        if add_item_form.is_valid():
            item_add = add_item_form.save(commit=False)
            item_add.list = to_do_list
            item_add.save()
            messages.success(
                self.request,
                f'YOUR TO-DO ITEM HAS BEEN CREATED SUCCESSFULLY'
                )

            url = reverse('to-do-items', args=[item_add.list.id])
            return redirect(url)


class CompleteItemView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        item = get_object_or_404(ToDoItem, pk=pk)
        item.complete = not item.complete
        item.save()

        if item.complete:
            messages.success(
                self.request,
                f'YOUR TO-DO ITEM HAS BEEN CLOSED SUCCESSFULLY'
                )
        else:
            messages.success(
                self.request,
                f'YOUR TO-DO ITEM HAS BEEN OPENED SUCCESSFULLY'
                )

        url = reverse('to-do-items', args=[item.list.id])
        return redirect(url)

    # validate request user is author and restrict if not
    def test_func(self):
        item = get_object_or_404(ToDoItem, pk=self.kwargs['pk'])
        return self.request.user == item.list.user


class DeleteItemView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        item = get_object_or_404(ToDoItem, pk=pk)
        item.delete()
        messages.success(
                self.request,
                f'YOUR TO-DO ITEM HAS BEEN DELETED SUCCESSFULLY'
                )

        url = reverse('to-do-items', args=[item.list.id])
        return redirect(url)

    # validate request user is author and restrict if not
    def test_func(self):
        item = get_object_or_404(ToDoItem, pk=self.kwargs['pk'])
        return self.request.user == item.list.user
