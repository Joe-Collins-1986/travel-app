from django.test import TestCase
from site_updates.models import UpdateCatagory, Update, UpdateComment
from django.contrib.auth.models import User
from django.urls import reverse


class TestUpdateCatagoryModels(TestCase):

    def setUp(self):
        self.catagory1 = UpdateCatagory.objects.create(
            topic_catagory='catagory-1'
        )

    def test_model_str_returns_topic_catagory_attribute(self):
        self.assertEquals(str(self.catagory1), 'catagory-1')


class TestUpdateModels(TestCase):

    def setUp(self):
        self.catagory1 = UpdateCatagory.objects.create(
            topic_catagory='catagory-1'
        )

        self.update1 = Update.objects.create(
            topic=self.catagory1,
            title='update-1',
            content='content information'
        )

    def test_foreign_key_link(self):
        self.assertEquals(self.update1.topic.topic_catagory, 'catagory-1')

    def test_model_str_returns_topic_catagory_attribute(self):
        self.assertEquals(str(self.update1), 'update-1')


class TestUpdateCommentModels(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(
            'JoeBloggs', 'JoeBloggs@test.com', 'Abc123456!')
        self.catagory1 = UpdateCatagory.objects.create(
            topic_catagory='catagory-1'
        )

        self.update1 = Update.objects.create(
            topic=self.catagory1,
            title='update-1',
            content='content information'
        )

        self.comment1 = UpdateComment.objects.create(
            site_update=self.update1,
            author=user1,
            title='test comment',
            comment='test comment content'
        )

        self.client.login(username='JoeBloggs', password='Abc123456!')

    def test_update_foreign_key_link(self):
        self.assertEquals(self.comment1.site_update.title, 'update-1')

    def test_user_foreign_key_link(self):
        self.assertEquals(self.comment1.author.username, 'JoeBloggs')

    def test_model_str_returns_update_comment_title_attribute(self):
        self.assertEquals(str(self.comment1), 'test comment')

    def test_model_update_comment_absolute_url_name(self):
        response = self.client.post(
            reverse(
                'admin-update-detail',
                args=[
                    self.comment1.site_update.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.comment1.get_absolute_url(),
                         f'/updates/{self.comment1.site_update.pk}/')
