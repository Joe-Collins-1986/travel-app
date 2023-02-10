from django.urls import path

from .views import (
    AdminUpdatesListView,
    AdminDetailUpdateView,
)

urlpatterns = [
    path('', AdminUpdatesListView.as_view(), name="all-admin-updates"),
    path('<int:pk>/', AdminDetailUpdateView.as_view(), name="admin-update-detail"),
]