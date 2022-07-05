from django.contrib import admin
from .models import Album, Favorite
from django.db import models
# Register your models here.
admin.site.register(Album)
admin.site.register(Favorite)