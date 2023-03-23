from .models import ToDoList, ToDoItem
from django import forms


class FullToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'description']


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['item']
