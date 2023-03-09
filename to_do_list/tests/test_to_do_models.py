from django.test import TestCase
from diary.models import Country
from to_do_list.models import ToDoList, ToDoItem
from django.contrib.auth.models import User
# from django.urls import reverse



class TestToDoListandToDoItemModel(TestCase):

    def setUp(self):

        user1 = User.objects.create_user(
            'JoeBloggs',
            'JoeBloggs@test.com',
            'Abc123456!')

        country1 = Country.objects.create(
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
            user=user1,
            country=country1,
            title="To Do List Title",
            description="To Do List Description",
        )

        self.to_do_item = ToDoItem.objects.create(
            list=self.to_do_list,
            item="To Do List Item",
        )
    
    def test_to_do_list_model_str_returns_title_attribute(self):
        self.assertEquals(str(self.to_do_list), 'To Do List Title')

    def test_to_do_item_model_str_returns_name_attribute(self):
        self.assertEquals(str(self.to_do_item), 'To Do List Item')

