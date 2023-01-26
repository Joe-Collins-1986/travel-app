from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import (
    View,
)


# Create your views here.
class TravelHome(View):
    def get(self, request):
            
        return render(
            request,
            "home/travel-home.html",
            {
                "tab_title": "Home"

            },
        )
