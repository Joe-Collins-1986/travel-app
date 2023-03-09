from django.test import TestCase, Client
from django.urls import reverse
from diary.models import Country
from to_do_list.models import ToDoList, ToDoItem
from to_do_list.forms import FullToDoListForm, ToDoItemForm
from django.contrib.auth.models import User


class TestToDoListViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
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

        self.to_do_list = ToDoList.objects.create(
            user=self.user1,
            country=self.country1,
            title="To Do List Title",
            description="To Do List Description",
        )

        self.url = reverse('to-do-lists', args=[self.country1.pk])

    def test_get_to_do_lists(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_to_do_lists_not_signed_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_post_to_do_lists(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        data = {
            'title': 'New To Do List Title', 
            'description': 'New To Do List Description',
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(
            response,
            reverse('to-do-lists', args=[self.country1.pk]),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertTrue(ToDoList.objects.filter(title='New To Do List Title').exists())

    def test_post_to_do_lists_not_loged_in(self):
        data = {
            'title': 'New To Do List Title', 
            'description': 'New To Do List Description',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(ToDoList.objects.filter(title='New To Do List Title').exists())

    def test_post_to_do_lists_invalid(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        data = {
            'title': '', 
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ToDoList.objects.filter(title='New To Do List Title').exists())

    def test_delete_list(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        url = reverse('delete-list', args=[self.to_do_list.pk])
        response = self.client.get(url)
        self.assertRedirects(
            response,
            reverse('to-do-lists', args=[self.country1.pk]),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertFalse(ToDoList.objects.filter(title='To Do List Title').exists())

    def test_delete_list_not_logged_in(self):
        url = reverse('delete-list', args=[self.to_do_list.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ToDoList.objects.filter(title='To Do List Title').exists())

    def test_delete_list_wrong_user(self):
        self.client.login(username='JaneBloggs', password='Xyz123456!')
        url = reverse('delete-list', args=[self.to_do_list.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ToDoList.objects.filter(title='To Do List Title').exists())


