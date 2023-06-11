from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class SoundModel(models.Model):
    main = models.FileField(upload_to='./files/')
    sourceType = models.CharField(max_length=200)
    sourceFile = models.FileField(upload_to='./files/')

class UserSoundModel(models.Model):
    userID = models.IntegerField()
    soundID = models.IntegerField()

admin.site.register(SoundModel)
admin.site.register(UserSoundModel)
