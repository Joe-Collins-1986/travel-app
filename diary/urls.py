from django.urls import path
from .views import (
    MapView,
    CountryView,
)

urlpatterns = [
    path('', MapView.as_view(), name="country-map"),
    path('country/<int:pk>', CountryView.as_view(), name="country"),
    
]