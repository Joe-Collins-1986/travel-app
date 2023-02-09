from django.shortcuts import render
from .models import Update
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
)


class AdminUpdatesListView(LoginRequiredMixin, ListView):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    model = Update
    template_name = 'site_updates/admin-updates.html'
    context_object_name = 'updates' # would pass object if not changed to post. Then would need to reference object not post in the template (see PostDetailView class for example)
    ordering = ["-published_on"]
    paginate_by = 5
