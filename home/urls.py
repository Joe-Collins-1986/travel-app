from django.urls import path
from .views import (
    TravelHome,
    register,
)

urlpatterns = [
    path('', TravelHome.as_view(), name="travel-home"),
    path('register/', register, name='travel-register'),

]