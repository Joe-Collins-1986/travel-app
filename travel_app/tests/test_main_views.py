from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class CustomErrorViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='JoeBloggs',
            password='Abc123456!'
        )

    def test_page_not_found_view(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        url = '/updates/654654/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
