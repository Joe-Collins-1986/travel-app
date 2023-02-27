from django.shortcuts import render, get_object_or_404
from .models import Profile
from diary.models import Visit, Country
from django.views.generic import (
    View,
)

# Create your views here.
class ProfilePageView(View):  

    def get(self, request):
        profile = get_object_or_404(Profile, user=self.request.user)

        countries = Visit.objects.filter(user=request.user.id)

        return render(
            request,
            "user_profile/profile.html",
            {
                "profile": profile,
                "countries": countries,
            }
        )