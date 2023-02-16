from django.shortcuts import render, get_object_or_404
from .models import Update, UpdateComment
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    View,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import CommentForm

class AdminUpdatesListView(ListView):
    # model = Update
    # template_name = 'site_updates/admin-updates.html'  # This takes the place of the defaul which would be: <app>/<model>_<viewtype>.html - therefore(blog/post_list.html)
    # context_object_name = 'updates' # would pass object if not changed to post. Then would need to reference object not post in the template (see PostDetailView class for example)
    # ordering = ["-published_on"]
    # paginate_by = 3


    

    def get(self, request):
        update_list = Update.objects.filter(status=1)
        page = request.GET.get('page', 1)
        paginator = Paginator(update_list, 2)

        try:
            updates = paginator.page(page)
        except PageNotAnInteger:
            updates = paginator.page(1)
        except EmptyPage:
            updates = paginator.page(paginator.num_pages)

        return render(
            request,
            "site_updates/admin-updates.html",
            {
                "updates": updates,
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

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # default to <app>/<model>_<form>.html
    model = UpdateComment
    context_object_name = 'comment'
    fields = ['title', 'comment', 'comment_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()

        if self.request.user == comment.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # default to a form for: <app>/<model>_<confirm_delete>.html
    model = UpdateComment
    context_object_name = 'comment'
    
    
    def get_success_url(self):
        comment = self.get_object()
        return reverse('admin-update-detail', args=[str(comment.site_update.id)])

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False