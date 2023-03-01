from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from taggit.managers import TaggableManager
from django_resized import ResizedImageField


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, default=None)
    country_image = models.ImageField(default=None, upload_to='media/country_pics/', blank=True)
    country_flag = models.ImageField(default=None, upload_to='media/country_maps/', blank=True)
    code = models.CharField(max_length=5, unique=True, default=None)
    capital = models.CharField(max_length=100, unique=True, default=None)
    region = models.CharField(max_length=100, default=None)
    currency = models.CharField(max_length=100, default=None)
    language = models.CharField(max_length=100, default=None)
    about = models.CharField(max_length=500, default=None)
    population = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="users_map")
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name="country_map")
    status = models.CharField(max_length=50, default="not_visited")

    def __str__(self):
        return self.status


EXPERIENCE_CHOICES = (
    ('Not Rated','Not Rated'),
    ('Amazing', 'Amazing'),
    ('Good','Good'),
    ('Meh','Meh'),
    ('Bad','Bad'),
    ('Awful','Awful'),
)


class Diary(models.Model):
    country = models.ForeignKey(
                                Country,
                                on_delete=models.CASCADE,
                                related_name="country_diary")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    content_image = ResizedImageField(
                                        upload_to='media/diary_pics/',
                                        blank=True,
                                        size=[600, None],
                                        force_format='JPEG')
    exp_rating = models.CharField(
                                    max_length=15,
                                    choices=EXPERIENCE_CHOICES,
                                    default='Not Rated')
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f'{self.created_on} diary post'