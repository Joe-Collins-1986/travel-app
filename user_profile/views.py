from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib import messages
from diary.models import Visit, Country
from django.views.generic import (
    View,
)
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class ProfilePageView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        profile = get_object_or_404(Profile, user=self.request.user)
        countries = Visit.objects.filter(user=request.user.id)
        countries = countries.filter(status='wish_list')

        return render(
            request,
            "user_profile/profile.html",
            {
                "profile": profile,
                "countries": countries,
            }
        )


class UpdateProfilePageView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        return render(
            request,
            "user_profile/update_profile.html",
            {
                "u_form": u_form,
                "p_form": p_form,
            }
        )

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)

        # form valid actions
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                self.request,
                'YOUR PROFILE HAS BEEN UPDATED SUCCESSFULLY'
                )
            return redirect('profile-page')

        else:
            return render(
                request,
                "user_profile/update_profile.html",
                {
                    "u_form": u_form,
                    "p_form": p_form,
                }
            )
