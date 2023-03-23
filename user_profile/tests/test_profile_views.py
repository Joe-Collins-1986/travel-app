from django.test import TestCase, Client
from user_profile.models import Profile
from django.urls import reverse
from diary.models import Country, Visit
from django.contrib.auth.models import User
import json

from django.shortcuts import render, get_object_or_404, redirect


class TestProfileView(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            'JoeBloggs',
            'JoeBloggs@test.com',
            'Abc123456!'
        )
        self.client = Client()

        with open('countries.json', 'r') as f:
            countries = json.load(f)
            f.close()

        for country in countries:
            Country.objects.create(
                name=country['name'],
                code=country['code'],
                capital=country['capital'],
                region=country['region'],
                currency=country['currency'],
                language=country['language'],
                about=country['about'],
                population=country['population']),

        visited_model = Visit.objects.create(
            user=user,
            country=Country.objects.get(code='AL'),
            status='wish_list')

    def test_profile_returns_user_data_and_wish_list(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(reverse('profile-page'))
        self.assertEqual(response.status_code, 200)


class TestUpdateProfilePageView(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            'JoeBloggs',
            'JoeBloggs@test.com',
            'Abc123456!'
        )
        self.client = Client()

        self.url = reverse('update-profile-page')

    def test_get(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/update_profile.html')

    def test_post_valid(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        data = {
            'username': 'newusername',
            'email': 'newemail@example.com',
            'objectives': 'new objectives',
            'background_img': 'media/profiles/background/rome-profile-bg.jpg'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile-page'))

        self.assertTrue(Profile.objects.filter(
            objectives='new objectives').exists())

        self.assertTrue(User.objects.filter(
            username='newusername',
            email='newemail@example.com').exists())

    def test_post_request_with_invalid_data(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        data = {
            'username': '',
            'email': 'invalidemail',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/update_profile.html')
        self.assertFormError(
            response,
            'u_form',
            'username',
            'This field is required.')
        self.assertFormError(
            response,
            'u_form',
            'email',
            'Enter a valid email address.')
