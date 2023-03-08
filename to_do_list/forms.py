from .models import ToDoList, ToDoItem
from django import forms


class FullToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'desription']


class CompleteToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['complete']


class FullToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['item', 'complete']


class CompleteToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['complete']