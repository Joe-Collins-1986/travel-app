from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


PROFILE_BACKGROUNDS = (
    ('media/profiles/background/profile-bg-default.jpg', 'Paris'),
    ('media/profiles/background/rome-profile-bg.jpg', 'Rome'),
    ('media/profiles/background/london-profile-bg.jpg', 'London'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = ResizedImageField(
                                default='media/profiles/default-profile-img.jpeg',
                                upload_to='media/profiles/',
                                size=[300, None],
                                force_format='JPEG')

    objectives = models.TextField(blank=True, null=True)

    background_img = models.CharField(
                                max_length=100,
                                choices=PROFILE_BACKGROUNDS,
                                default='media/profiles/background/profile-bg-default.jpg')

    def __str__(self):
        return f"{self.user.username} Profile"


