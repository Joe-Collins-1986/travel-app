from django.test import TestCase, Client
from django.urls import reverse
from diary.models import Country, Visit, Diary
from django.contrib.auth.models import User
import json


class TestMapView(TestCase):
    """ Test Map View """

    def setUp(self):
        user1 = User.objects.create_user('JoeBloggs',
                                         'JoeBloggs@test.com',
                                         'Abc123456!')
        self.client = Client()
        self.client.id = 1

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
                                   population=country['population']),

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
    

class TestCountryView(TestCase):

    def setUp(self):
        user1 = User.objects.create_user('JoeBloggs',
                                         'JoeBloggs@test.com',
                                         'Abc123456!')
        self.client = Client()
        self.client.id = 1

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

        self.visited_model = Visit.objects.create(user=user1,
                                                  country=Country.objects.get(code='AL'),
                                                  status='visited')

    def test_get_country_info_not_visited_found(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(reverse('country', args=[10]))
        self.assertEqual(response.status_code, 200)
    
    def test_get_country_info__visited_found(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(reverse('country', args=[self.visited_model.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_valid_visited_form_for_visted_user(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.post(reverse('country',
                                    args=[self.visited_model.id]),
                                    data={'status': 'wish_list'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f'/diary/country/{self.visited_model.id}',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_post_invalid_visited_form_for_visted_user(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.post(reverse('country',
                                    args=[self.visited_model.id]))
        self.assertEqual(response.status_code, 302)

    def test_post_valid_visited_form_for_non_visited_user(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.post(reverse('country',
                                    args=[2]),
                                    data={'status': 'wish_list'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f'/diary/country/2',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
    
    def test_post_invalid_visited_form_for_non_visted_user(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.post(reverse('country',
                                    args=[2]))
        self.assertEqual(response.status_code, 302)


class TestDiaryAllPostsView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'JoeBloggs',
            'JoeBloggs@test.com',
            'Abc123456!')

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

        self.url = reverse('diary-all-posts', args=[self.country1.pk])
        self.url_pagination_not_int = f'{self.url}?page=t'
        self.url_pagination_empty_page = f'{self.url}?page=9999'

    def test_diary_all_posts_list(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_with_search_query(self):
        response = self.client.get(self.url, {"q": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test content")

    def test_get_not_int_pagination(self):
        response = self.client.get(self.url_pagination_not_int)
        self.assertEqual(response.status_code, 200)

    def test_get_empty_page_pagination(self):
        response = self.client.get(self.url_pagination_empty_page)
        self.assertEqual(response.status_code, 200)


class DiaryTagsView(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            'JoeBloggs',
            'JoeBloggs@test.com',
            'Abc123456!')

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
        self.url = reverse('diary-tags', args=[self.country1.pk])
        self.url_pagination_not_int = f'{self.url}?page=t'
        self.url_pagination_empty_page = f'{self.url}?page=9999'

    def test_diary_tags_list(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_not_int_pagination(self):
        response = self.client.get(self.url_pagination_not_int)
        self.assertEqual(response.status_code, 200)

    def test_get_empty_page_pagination(self):
        response = self.client.get(self.url_pagination_empty_page)
        self.assertEqual(response.status_code, 200)


class TestDiaryCreateView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
                'JoeBloggs',
                'JoeBloggs@test.com',
                'Abc123456!')

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

        self.url = reverse('diary-create', kwargs={'pk': self.country1.pk})

    def test_post_valid_no_tags(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        data = {
            'content': 'Test diary post content', 
            'exp_rating': 'Not Rated',
            'tags': [''],
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(
            response,
            reverse('diary-all-posts', args=[self.country1.pk]),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertTrue(Diary.objects.filter(content='Test diary post content').exists())

    def test_post_valid_tags(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        data = {
            'content': 'Test diary post content', 
            'exp_rating': 'Not Rated',
            'tags': ['Test_Tag_1', 'Test_Tag_2'],
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(
            response,
            reverse('diary-all-posts', args=[self.country1.pk]),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertTrue(Diary.objects.filter(content='Test diary post content').exists())



class TestDiaryUpdateView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
                'JoeBloggs',
                'JoeBloggs@test.com',
                'Abc123456!')

        self.user2 = User.objects.create_user(
                'JaneBloggs',
                'JaneBloggs@test.com',
                'Xyz123456!')

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
            content='Test diary post content', 
            exp_rating='Not Rated',
            author=self.user,
            country=self.country1
        )

        self.url = reverse('diary-update', kwargs={'pk': self.country1.pk})

    def test_post_valid(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        self.url = reverse('diary-update', kwargs={'pk': self.diary.pk})
        data = {
            'content': 'Updated test content', 
            'exp_rating': 'Not Rated',
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(
            response,
            reverse('diary-all-posts', args=[self.country1.pk]),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertTrue(Diary.objects.filter(
            content='Updated test content').exists())

    def test_post_not_author(self):
        self.client.login(username='JaneBloggs', password='Xyz123456!')
        self.url = reverse('diary-update', kwargs={'pk': self.diary.pk})
        data = {
            'content': 'Update test content from another login user.',
            }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Diary.objects.filter(
            content='Test diary post content').exists())
        self.assertFalse(Diary.objects.filter(
            content='Update test content from another login user.').exists())


class TestDiaryDeleteView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
                'JoeBloggs',
                'JoeBloggs@test.com',
                'Abc123456!')

        self.user2 = User.objects.create_user(
                'JaneBloggs',
                'JaneBloggs@test.com',
                'Xyz123456!')

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
            content='Test diary post content', 
            exp_rating='Not Rated',
            author=self.user,
            country=self.country1
        )

        self.url = reverse('diary-delete', kwargs={'pk': self.diary.pk})

    def test_post_valid(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        self.url = reverse('diary-delete', kwargs={'pk': self.diary.pk})

        response = self.client.post(self.url)
        self.assertRedirects(
            response,
            reverse('diary-all-posts', args=[self.country1.pk]),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertFalse(Diary.objects.filter(
            content='Updated test content').exists())

    def test_post_not_author(self):
        self.client.login(username='JaneBloggs', password='Xyz123456!')
        self.url = reverse('diary-delete', kwargs={'pk': self.diary.pk})
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Diary.objects.filter(
            content='Test diary post content').exists())