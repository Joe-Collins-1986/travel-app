from django.urls import path
from .views import (
    TravelHome,
)

urlpatterns = [
    path('', TravelHome.as_view(), name="travel-home"),

]