from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_register_GET(self):
        client = Client()
        response = client.get(reverse('travel-register'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/register.html')