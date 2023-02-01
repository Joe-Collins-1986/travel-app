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
]