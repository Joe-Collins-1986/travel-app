from django.test import TestCase
from diary.models import Country, Visit
from django.contrib.auth.models import User


class TestCountryModel(TestCase):

    def setUp(self):
        self.country1 = Country.objects.create(
            name='country-1',
            code='AA',
            capital='Capital',
            region='Region',
            currency='Pounds',
            language='English',
            about='Test content',
            population='Sixy thousand',
        )

    def test_country_model_str_returns_country_name_attribute(self):
        self.assertEquals(str(self.country1), 'country-1')


class TestVisitModel(TestCase):

    def setUp(self):
        user1 = User.objects.create_user('JoeBloggs', 'JoeBloggs@test.com', 'Abc123456!')
        self.country1 = Country.objects.create(
            name='country-1',
            code='AA',
            capital='Capital',
            region='Region',
            currency='Pounds',
            language='English',
            about='Test content',
            population='Sixy thousand',
        )

        self.visited_example = Visit.objects.create(
            country=self.country1,
            status='visited',
            user=user1
        )

    def test_visit_foreign_key_country_link(self):
        self.assertEquals(self.visited_example.country.name, 'country-1')

    def test_visit_foreign_key_user_link(self):
        self.assertEquals(str(self.visited_example.user), 'JoeBloggs')

    def test_visit_model_str_returns_visit_status_attribute(self):
        self.assertEquals(str(self.visited_example), 'visited')
