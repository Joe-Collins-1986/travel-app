from django.test import TestCase
from user_profile.models import Profile
from django.contrib.auth.models import User


class TestProfileModel(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user('JoeBloggs', 'JoeBloggs@test.com', 'Abc123456!')

    def test_profile_created_on_user_registraiton(self):
        self.assertIsInstance(self.user.profile, Profile)

    def test_profile_str(self):
        self.assertEquals(str(self.user.profile), 'JoeBloggs Profile')
