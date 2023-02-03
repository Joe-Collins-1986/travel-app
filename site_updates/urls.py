from django.urls import path

from .views import (
    AdminUpdatesListView,
)

urlpatterns = [
    path('', AdminUpdatesListView.as_view(), name="all-admin-updates"),
]