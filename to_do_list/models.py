from django.db import models
from django.contrib.auth.models import User
from diary.models import Country

# Create your models here.


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name="country_to_do")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ['complete']
