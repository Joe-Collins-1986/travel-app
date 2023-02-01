from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to log in under username: {username}!")
            return redirect('home-login')
    else:
        form = UserRegisterForm()

    return render(
                request,
                'home/register.html',
                {
                    "tab_title": "Register",
                    "form": form
                }
            )
