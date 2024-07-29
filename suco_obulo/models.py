from django.db import models
from django.contrib.auth.models import User

from suco_obulo.thumbnail_img import make_thumbnail


class Page(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/obulo_images")
    page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Save image in small quality
    def save(self, *args, **kwargs):
        self.image = make_thumbnail(self.image, size=(1200, 1200))
        return super().save(*args, **kwargs)