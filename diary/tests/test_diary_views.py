from django.test import TestCase, Client
from django.urls import reverse
from diary.models import Country, Visit
from django.contrib.auth.models import User
import json


class TestMapView(TestCase):
    """ Test Map View """

    def setUp(self):
        user1=User.objects.create_user('JoeBloggs',
                                        'JoeBloggs@test.com',
                                        'Abc123456!')
        self.client = Client()
        self.client.id=1

        with open('countries.json', 'r') as f:
            countries = json.load(f)
            f.close()
        
        for country in countries:
            Country.objects.create(name=country['name'],
                                   code=country['code'],
                                   capital=country['capital'],
                                   region=country['region'],
                                   currency=country['currency'],
                                   language=country['language'],
                                   about=country['about'],
                                   population=country['population'])

        country_code_list = []

        for country in countries:
            country_code_list.append(country['code'])

        visited_model = Visit.objects.create(user=user1,
                                             country=Country.objects.get(code='AL'),
                                             status='visited')

    def test_map_get_function(self):
        """ Test loading of map page """
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(reverse('country-map'))
        self.assertEqual(response.status_code, 200)
    

