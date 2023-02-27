from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = ResizedImageField(
                                default='media/profiles/default-profile-img.jpeg',
                                upload_to='media/profiles/',
                                size=[300, None],
                                force_format='JPEG')

    objectives = models.TextField(blank=True, null=True)

    background_img = ResizedImageField(
                                default='media/profiles/background/profile-bg-default.jpg',
                                upload_to='media/profiles/background/',
                                size=[1920, None],
                                force_format='JPEG')



    def __str__(self):
        return f"{self.user.username} Profile"


