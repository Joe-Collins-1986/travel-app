from django.shortcuts import render
from .models import Update
from django.views.generic import (
    ListView,
)


class AdminUpdatesListView(ListView):

    model = Update
    template_name = 'site_updates/admin-updates.html'
    context_object_name = 'updates' # would pass object if not changed to post. Then would need to reference object not post in the template (see PostDetailView class for example)
    ordering = ["-published_on"]
    paginate_by = 5
