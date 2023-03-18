from django.urls import path, re_path
from .views import (
    MapView,
    CountryView,
    DiaryAllPostsView,
    DiaryTagsView,
    DiaryCreateView,
    DiaryUpdateView,
    DiaryDeleteView,
)

urlpatterns = [
    path('', MapView.as_view(), name="country-map"),
    path('country/<int:pk>',CountryView.as_view(), name="country"),

    path('diary_all_posts/<int:pk>', DiaryAllPostsView.as_view(), name="diary-all-posts"),
    path('diary_tags/<int:pk>', DiaryTagsView.as_view(), name="diary-tags"),

    path('diary/<int:pk>/new/', DiaryCreateView.as_view(
            extra_context={
                              "tab_title": "Create Post",
                           }
         ), name="diary-create"),
    path('diary/<int:pk>/update/', DiaryUpdateView.as_view(
            extra_context={
                              "tab_title": "Update Post",
                           }
        ), name="diary-update"),
    path('diary/<int:pk>/delete/', DiaryDeleteView.as_view(
            extra_context={
                              "tab_title": "Delete Post",
                           }
        ), name="diary-delete"),
]