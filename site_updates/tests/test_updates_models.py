from django.test import TestCase
from site_updates.models import UpdateCatagory, Update


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




