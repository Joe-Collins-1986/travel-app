from django.db import models
from PIL import Image

STATUS = ((0, "Draft"), (1, "Published"))


class UpdateCatagory(models.Model):
    topic_catagory = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_catagory


class Update(models.Model):
    topic = models.ForeignKey(UpdateCatagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    update_image = models.ImageField(default=None, upload_to='media/update_pics/')
    published_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-published_on',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('update-detail', args=[str(self.update.id)])