from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class TestRegister(TestCase):
    """ Test Register Function """

    def test_register_user_get(self):
        """ Test loading of register page """
        response = self.client.get(reverse('home-register'))
        self.assertEqual(response.status_code, 200)

    def test_register_user_valid_input(self):
        """ Test redirection when user registers succesfully """
        response = self.client.post(reverse('home-register'), data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456!',
            'password2': 'Abc123456!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_register_user_invalid(self):
        """ Test redirect if user is invalid """
        response = self.client.post(reverse('home-register'), data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456!',
            'password2': 'IncorrectPassword'
        })
        self.assertEqual(response.status_code, 200)


class TestLogin(TestCase):
    """ Test Login Function """

    def setUp(self):
        """ Setup to test login """
        self.user = User.objects.create_user(
            username='JoeBloggs',
            email='JoeBloggs@test.com',
            password='Abc123456!')

    def test_login_user_get(self):
        """ Test loading of login page """
        response = self.client.get(reverse('home-login'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_user_post_valid_input(self):
        """ Test redirection when user login succesful """
        response = self.client.post(reverse('home-login'), data={
            'username': 'JoeBloggs',
            'password': 'Abc123456!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        
    def test_login_user_post_invalid_username_input(self):
        """ Test redirection when user login succesful """
        response = self.client.post(reverse('home-login'), data={
            'username': 'IncorrectUserName',
            'password': 'Abc123456!',
        })
        self.assertEqual(response.status_code, 200)
    
    def test_login_user_post_invalid_password_input(self):
        """ Test redirection when user login succesful """
        response = self.client.post(reverse('home-login'), data={
            'username': 'JoeBloggs',
            'password': 'IncorrectPassword',
        })
        self.assertEqual(response.status_code, 200)
    


class TestHome(TestCase):

    def setUp(self):
        User.objects.create_user('JoeBloggs', 'JoeBloggs@test.com', 'Abc123456!')
        self.client = Client()

    def test_home_view_redirects_non_authenticated_users_to_login_page(self):
        response = self.client.get(reverse('travel-home'))
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200
            )
    
    def test_home_view_for_authenticated_user(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(reverse('travel-home'))
        self.assertEqual(response.status_code, 200)
    