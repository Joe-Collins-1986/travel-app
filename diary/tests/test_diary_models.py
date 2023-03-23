from django.test import TestCase
from diary.models import Country, Visit, Diary
from django.contrib.auth.models import User
from django.urls import reverse


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
        user1 = User.objects.create_user(
            'JoeBloggs', 'JoeBloggs@test.com', 'Abc123456!')
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


class TestDiaryModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'JoeBloggs', 'JoeBloggs@test.com', 'Abc123456!')

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

        self.diary = Diary.objects.create(
            country=self.country1,
            author=self.user,
            content="test content"
        )

        self.client.login(username='JoeBloggs', password='Abc123456!')

    def test_diary_model_str(self):
        date_created = self.diary.created_on
        self.assertEquals(str(self.diary), f'{date_created} diary post')

    def test_diary_absolute_url_name(self):
        response = self.client.post(
            reverse(
                'diary-all-posts',
                args=[
                    self.country1.id]))
        self.assertEqual(self.diary.get_absolute_url(),
                         f'/diary/diary_all_posts/{self.country1.pk}')
