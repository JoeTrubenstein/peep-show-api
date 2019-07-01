from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    excerpt = models.TextField(default=" ")
    image = models.CharField(default=" ", max_length=800)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=800)
    image = models.CharField(max_length=800)
    occupation = models.TextField(default=" ")
    relationships = models.TextField(default=" ")
    quotes = ArrayField(models.CharField(max_length=200), blank=True)

    

    def __str__(self):
        return self.name
