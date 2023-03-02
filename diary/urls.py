from django.urls import path
from .views import (
    MapView,
    CountryView,
    DiaryAllPostsView,
    DiaryTagsView,
    DiaryCreateView,
    DiaryUpdateView,
)

urlpatterns = [
    path('', MapView.as_view(), name="country-map"),
    path('country/<int:pk>', CountryView.as_view(), name="country"),

    path('diary_all_posts/<int:pk>', DiaryAllPostsView.as_view(), name="diary-all-posts"),
    path('diary_tags/<int:pk>', DiaryTagsView.as_view(), name="diary-tags"),

    path('diary/<int:pk>/new/', DiaryCreateView.as_view(), name="diary-create"),
    path('diary/<int:pk>/update/', DiaryUpdateView.as_view(), name="diary-update"),
]