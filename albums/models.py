from urllib import request
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def check_is_user_favorite(self, user):
        for favorite in self.favorites.all():
            if favorite.album == self:
                return True

class User(AbstractUser):
    pass

class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="favorites", null=True, blank=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="favorites", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

