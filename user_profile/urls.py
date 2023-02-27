from django.urls import path

from .views import (
    ProfilePageView,
    UpdateProfilePageView,
)

urlpatterns = [
    path('', ProfilePageView.as_view(), name="profile-page"),
    path('update_profile/', UpdateProfilePageView.as_view(), name="update-profile-page"),

]