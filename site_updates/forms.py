from .models import UpdateComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = UpdateComment
        fields = ['title', 'comment', 'comment_image']