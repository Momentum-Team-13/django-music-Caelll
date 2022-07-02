from urllib import request
from django.db import models
from django.utils import timezone

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title


