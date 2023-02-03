from django.urls import path
from django.contrib.auth import views as auth_views

from site_updates.models import Update

from .views import (
    TravelHome,
    register,
)

updates = Update.objects.filter(status=1).order_by('-published_on')[0:3]

urlpatterns = [
    path('', TravelHome.as_view(), name="travel-home"),
    path('register/', register, name='home-register'),
    path('login/',
         auth_views.LoginView.as_view(
            template_name='home/login.html',
            extra_context={
                              "tab_title": "Login",
                              "updates": updates,
                           }
         ),
         name='home-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='home-logout'),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(
            template_name='home/password_reset.html',
            extra_context={
                              "tab_title": "Reset",
                              "updates": updates,
                           }),
         name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='home/password_reset_confirm.html',
            extra_context={
                              "tab_title": "Update Password",
                              "updates": updates,
                           }),
         name='password_reset_confirm'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='home/password_reset_done.html',
            extra_context={
                              "tab_title": "Email Sent",
                              "updates": updates,
                           }),
         name='password_reset_done'),

    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='home/password_reset_complete.html',
            extra_context={
                              "tab_title": "Password Updated",
                              "updates": updates,
                           }),
         name='password_reset_complete'),
]