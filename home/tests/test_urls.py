from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from home.views import (
    register,
    TravelHome,
)


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('travel-home')
        self.assertEquals(resolve(url).func.view_class, TravelHome)
    
    def test_register_url_resolves(self):
        url = reverse('home-register')
        self.assertEquals(resolve(url).func, register)

    def test_login_url_resolves(self):
        url = reverse('home-login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_resolves(self):
        url = reverse('home-logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)


