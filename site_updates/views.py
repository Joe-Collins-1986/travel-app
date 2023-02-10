from django.shortcuts import render, get_object_or_404
from .models import Update, UpdateComment
from django.views.generic import (
    ListView,
    View,
)
from .forms import CommentForm

class AdminUpdatesListView(ListView):

    model = Update
    template_name = 'site_updates/admin-updates.html'
    context_object_name = 'updates' # would pass object if not changed to post. Then would need to reference object not post in the template (see PostDetailView class for example)
    ordering = ["-published_on"]
    paginate_by = 5


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