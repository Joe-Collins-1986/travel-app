from django.shortcuts import render, get_object_or_404
from .models import Update, UpdateComment
from django.views.generic import (
    View,
    UpdateView
)
from .forms import CommentForm

class AdminUpdatesListView(View):

    def get(self, request):
        update_objects = Update.objects.filter(status=1)

        return render(
            request,
            "site_updates/admin-updates.html",
            {
                "updates": update_objects,
            }
        )


class AdminDetailUpdateView(View):

    def get(self, request, pk):
        update_objects = Update.objects.filter(status=1)
        update = get_object_or_404(update_objects, pk=pk)
        comments = UpdateComment.objects.filter(site_update=update)

        for comment in comments:
            a = str(comment.updated_on - comment.created_on)
            if '0:00:00' in a:
                comment.updated_on = None

        return render(
            request,
            "site_updates/admin-update-detail.html",
            {
                "update": update,
                "comments": comments,
                "comment_form": CommentForm()
            }
        )
    
    def post(self, request, pk):
        update_objects = Update.objects.filter(status=1)
        update = get_object_or_404(update_objects, pk=pk)
        comments = UpdateComment.objects.filter(site_update=update)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.site_update = update
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            "site_updates/admin-update-detail.html",
            {
                "update": update,
                "comments": comments,
                "comment_form": CommentForm()
            }
        )

class CommentUpdateView(UpdateView): # create and update will default to <app>/<model>_<form>.html - same template as create
    model = UpdateComment
    fields = ['title', 'comment', 'comment_image']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user.username == comment.name:
            return True
        return False