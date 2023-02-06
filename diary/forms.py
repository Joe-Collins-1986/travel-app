from .models import Visit
from django import forms


VISITED = [
    ('not_visited', 'Not Visited'),
    ('visited', 'Visited'),
    ('wish_list', 'Wish List'),
    ]

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['status',]
    
    status = forms.CharField(label="Have you visited this counry before? Do you want to?", widget=forms.Select(choices=VISITED))
