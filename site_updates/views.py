from django.shortcuts import render, get_object_or_404
from .models import Update, UpdateComment, UpdateCatagory
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    View,
    UpdateView,
    DeleteView,
    CreateView,
)
from .forms import CommentForm


class AdminUpdatesListView(View):

    def get(self, request):
        topics = UpdateCatagory.objects.all()

        # filter results
        if request.GET.get('q') is not None:
            q = request.GET.get('q')
        else:
            q = ""

        update_list_published = Update.objects.all()

        updates = update_list_published.filter(
            Q(topic__topic_catagory__icontains=q) |
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )

        # remove object duplication from filter
        updates = updates.distinct()

        topic_items = updates.count()

        # pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(updates, 5)

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
                "search_query": q,
                "tab_title": "Site Updates"
            }
        )


class AdminDetailUpdateView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        update_objects = Update.objects.all()
        update = get_object_or_404(update_objects, pk=pk)
        comments = UpdateComment.objects.filter(site_update=update)

        # if created and updated are equal set updated_on to none
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
                "comment_form": CommentForm(),
                "tab_title": "Update"
            }
        )

    def post(self, request, pk):
        update_objects = Update.objects.all()
        update = get_object_or_404(update_objects, pk=pk)
        comments = UpdateComment.objects.filter(site_update=update)

        comment_form = CommentForm(request.POST, request.FILES or None)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.site_update = update
            comment.save()
            messages.success(
                self.request,
                'YOUR NEW COMMENT HAS BEEN CREATED SUCCESSFULLY'
                )
        else:
            comment_form = CommentForm()

        # if created and updated are equal set updated_on to none
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


class CommentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    model = UpdateComment
    fields = ['title', 'comment', 'comment_image']

    # valid from actions
    def form_valid(self, form):
        update = get_object_or_404(Update, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.site_update = update
        messages.success(
                self.request,
                'YOUR NEW COMMENT HAS BEEN CREATED SUCCESSFULLY'
                )
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    model = UpdateComment
    fields = ['title', 'comment', 'comment_image']

    # valid from actions
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
                self.request,
                'YOUR COMMENT HAS BEEN UPDATED SUCCESSFULLY'
                )
        return super().form_valid(form)

    # restrict if user is not author
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    model = UpdateComment
    context_object_name = 'comment'

    # navigate to update detail if successful
    def get_success_url(self):
        comment = self.get_object()
        messages.success(
                self.request,
                'YOUR COMMENT HAS BEEN DELETED SUCCESSFULLY'
                )
        return reverse('admin-update-detail',
                       args=[str(comment.site_update.id)])

    # restrict if user is not author
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
