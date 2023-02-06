from django.db import models
from PIL import Image


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, default=None)
    country_image = models.ImageField(default=None, upload_to='media/country_pics/', blank=True)
    country_map = models.ImageField(default=None, upload_to='media/country_maps/', blank=True)
    code = models.CharField(max_length=5, unique=True, default=None)
    capital = models.CharField(max_length=100, unique=True, default=None)
    region = models.CharField(max_length=100, default=None)
    currency = models.CharField(max_length=100, default=None)
    language = models.CharField(max_length=100, default=None)
    about = models.CharField(max_length=500, default=None)
    population = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name