from django.test import TestCase, Client
from django.urls import reverse
from site_updates.models import UpdateComment, UpdateCatagory, Update
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User


class AdminUpdatesListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("all-admin-updates")
        self.topic = UpdateCatagory.objects.create(topic_catagory="Test Topic")
        self.update = Update.objects.create(
            title="Test Update",
            content="Test Content",
            topic=self.topic
        )
        self.url_is_not_int = f"/updates/?page=t"
        self.url_is_blank = f"/updates/?page=99999"

    def test_get_with_search_query(self):
        response = self.client.get(self.url, {"q": "Test"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Update")
    
    def test_get_without_search_query(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_not_int_pagination(self):
        response = self.client.get(self.url_is_not_int)
        self.assertEqual(response.status_code, 200)

    def test_get_blank_pagination(self):
        response = self.client.get(self.url_is_blank)
        self.assertEqual(response.status_code, 200)


class AdminDetailUpdateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='JoeBloggs',
            password='Abc123456!'
        )
        self.catagory = UpdateCatagory.objects.create(
            topic_catagory='Test catagory'
        )
        self.update = Update.objects.create(
            topic=self.catagory,
            title='Test Update',
            content='Test content',
        )
        self.comment = UpdateComment.objects.create(
            title="Comment Title",
            comment='Test comment',
            author=self.user,
            site_update=self.update)
        self.url = reverse('admin-update-detail', kwargs={'pk': self.update.pk})

    def test_get(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site_updates/admin-update-detail.html')

    def test_post_valid(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        data = {
            'title': 'Comment Title 2', 
            'comment': 'Test Comment 2',
            }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site_updates/admin-update-detail.html')


class CommentCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='JoeBloggs',
            password='Abc123456!'
        )
        self.catagory = UpdateCatagory.objects.create(
            topic_catagory='Test catagory'
        )
        self.update = Update.objects.create(
            topic=self.catagory,
            title='Test Update',
            content='Test content',
        )
        self.url = reverse('admin-update-detail', kwargs={'pk': self.update.pk})

    def test_post_valid(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        self.url = reverse('comment-create', kwargs={'pk': self.update.pk})
        data = {
            'title': 'Test Comment', 
            'comment': 'This is a test comment.',
            }
        response = self.client.post(self.url, data)
        self.assertRedirects(
            response,
            reverse('admin-update-detail', kwargs={'pk': self.update.pk}),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertTrue(UpdateComment.objects.filter(title='Test Comment', comment='This is a test comment.').exists())


class CommentUpdateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='JoeBloggs',
            password='Abc123456!'
        )
        self.user2 = User.objects.create_user(
            username='JaneBloggs',
            password='Xyz123456!'
        )
        self.catagory = UpdateCatagory.objects.create(
            topic_catagory='Test catagory'
        )
        self.update = Update.objects.create(
            topic=self.catagory,
            title='Test Update',
            content='Test content',
        )
        self.comment = UpdateComment.objects.create(
            title="Comment Title",
            comment='Test comment',
            author=self.user,
            site_update=self.update)

    def test_post_valid(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        self.url = reverse('comment-update', kwargs={'pk': self.comment.pk})
        data = {
            'title': 'Updated Comment', 
            'comment': 'This is an update test comment.',
            }
        response = self.client.post(self.url, data)
        self.assertRedirects(
            response,
            reverse('admin-update-detail', kwargs={'pk': self.update.pk}),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertTrue(UpdateComment.objects.filter(
            title='Updated Comment',
            comment='This is an update test comment.').exists())

    def test_post_not_author(self):
        self.client.login(username='JaneBloggs', password='Xyz123456!')
        self.url = reverse('comment-update', kwargs={'pk': self.comment.pk})
        data = {
            'title': 'Updated Comment From Wrong Author', 
            'comment': 'Update test comment from another login user.',
            }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UpdateComment.objects.filter(
            title='Comment Title',
            comment='Test comment').exists())
        self.assertFalse(UpdateComment.objects.filter(
            title='Updated Comment From Wrong Author',
            comment='Update test comment from another login user.').exists())

class CommentDeleteViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='JoeBloggs',
            password='Abc123456!'
        )
        self.user2 = User.objects.create_user(
            username='JaneBloggs',
            password='Xyz123456!'
        )
        self.catagory = UpdateCatagory.objects.create(
            topic_catagory='Test catagory'
        )
        self.update = Update.objects.create(
            topic=self.catagory,
            title='Test Update',
            content='Test content',
        )
        self.comment = UpdateComment.objects.create(
            title="Comment Title",
            comment='Test comment',
            author=self.user,
            site_update=self.update)

    def test_delete_post_valid(self):
        self.client.login(username='JoeBloggs', password='Abc123456!')
        self.url = reverse('comment-delete', kwargs={'pk': self.comment.pk})
        response = self.client.post(self.url)
        self.assertRedirects(
            response,
            reverse('admin-update-detail', kwargs={'pk': self.update.pk}),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)
        self.assertFalse(UpdateComment.objects.filter(
            title='Comment Title',
            comment='Test comment').exists())

    def test_delete_post_not_author(self):
        self.client.login(username='JaneBloggs', password='Xyz123456!')
        self.url = reverse('comment-delete', kwargs={'pk': self.comment.pk})
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UpdateComment.objects.filter(
            title='Comment Title',
            comment='Test comment').exists())