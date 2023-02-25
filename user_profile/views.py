from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.views.generic import (
    View,
)

# Create your views here.
class ProfilePageView(View):  

    def get(self, request):
        profile = get_object_or_404(Profile, user=self.request.user)

        return render(
            request,
            "user_profile/profile.html",
            {
                "profile": profile,
            }
        )