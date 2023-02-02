from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    TravelHome,
    register,
)

urlpatterns = [
    path('', TravelHome.as_view(), name="travel-home"),
    path('register/', register, name='home-register'),
    path('login/',
         auth_views.LoginView.as_view(
            template_name='home/login.html',
            extra_context={"tab_title": "Login"}  # will need to import admin updates model and pass through as context
         ),
         name='home-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='home-logout'),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(
            template_name='home/password_reset.html'),
         name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='home/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='home/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='home/password_reset_complete.html'),
         name='password_reset_complete'),
]