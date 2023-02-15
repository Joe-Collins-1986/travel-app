from django.urls import path

from .views import (
    AdminUpdatesListView,
    AdminDetailUpdateView,
    CommentUpdateView,
)

urlpatterns = [
    path('', AdminUpdatesListView.as_view(), name="all-admin-updates"),
    path('<int:pk>/', AdminDetailUpdateView.as_view(), name="admin-update-detail"),

    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name="comment-update"),
]