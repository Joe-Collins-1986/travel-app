from django.test import TestCase
from django.urls import reverse


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

    def test_register_user_invalid(self):
        """ Test redirect if user is invalid """
        response = self.client.post(reverse('home-register'), data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456!',
            'password2': 'IncorrectPassword'
        })
        self.assertEqual(response.status_code, 200)
