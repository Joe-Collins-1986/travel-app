from django.urls import path

from .views import (
    AdminUpdatesListView,
    AdminDetailUpdateView,
    CommentUpdateView,
    CommentDeleteView,
    CommentCreateView,
)

urlpatterns = [
    path('', AdminUpdatesListView.as_view(), name="all-admin-updates"),
    path('<int:pk>/', AdminDetailUpdateView.as_view(), name="admin-update-detail"),

    path('comment/<int:pk>/new/', CommentCreateView.as_view(
            extra_context={
                              "tab_title": "Add Comment",
                           }
         ), name="comment-create"),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(
            extra_context={
                              "tab_title": "Update Comment",
                           }
         ), name="comment-update"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(
            extra_context={
                              "tab_title": "Delete Comment",
                           }
         ), name="comment-delete"),
]