from django.shortcuts import render, get_object_or_404
from .models import Update, UpdateComment, UpdateCatagory
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    View,
    UpdateView,
    DeleteView
)
from .forms import CommentForm


class AdminUpdatesListView(View):  

    def get(self, request):
        topics = UpdateCatagory.objects.all()

        if request.GET.get('q') is not None:
            q = request.GET.get('q')
        else:
            q = ""

        update_list_published = Update.objects.filter(status=1)

        update_list = update_list_published.filter(
            Q(topic__topic_catagory__icontains=q) |
            Q(title__icontains=q)
            )

        topic_items = update_list.count()

        updates = update_list

        if q == "":
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
                "topics": topics,
                "topic_items": topic_items,
                "all_published_updates": update_list_published,
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