from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from site_updates.models import Update

from .forms import UserRegisterForm
from django.views.generic import (
    View,
)


class TravelHome(View):

    def get(self, request):
        updates = Update.objects.all().order_by('-published_on')[0:3]

        if request.user.is_authenticated:
            return render(
                request,
                "home/travel-home.html",
                {
                    "tab_title": "Home",
                    "updates": updates,
                },
            )
        else:
            return redirect('home-login')


def register(request):
    updates = Update.objects.all().order_by('-published_on')[0:3]

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Your account has been created!")
            return redirect('travel-home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'home/register.html',
        {
            "tab_title": "Register",
            "form": form,
            "updates": updates,
        }
    )
