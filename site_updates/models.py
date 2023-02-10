from django.db import models
from django.contrib.auth.models import User
from PIL import Image

STATUS = ((0, "Draft"), (1, "Published"))
COMMENT_STATUS = ((0, "No Action Required"), (1, "Action Required"))


class UpdateCatagory(models.Model):
    topic_catagory = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_catagory


class Update(models.Model):
    topic = models.ForeignKey(UpdateCatagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    update_image = models.ImageField(default=None, upload_to='media/update_pics/', blank=True)
    published_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-published_on',)

    def __str__(self):
        return self.title


class UpdateComment(models.Model):
    site_update = models.ForeignKey(Update, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    comment = models.TextField()
    comment_image = models.ImageField(default=None, upload_to='media/comment_pics/', blank=True)
    action_taken = models.TextField(blank=True)
    action_image = models.ImageField(default=None, upload_to='media/comment_pics/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    comment_status = models.IntegerField(choices=COMMENT_STATUS, default=0)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title