from django.db import models

# Create your models here.
class Persona(models.Model):
    userID = models.TextField()
    mbti = models.TextField()
    artist = models.TextField()
    songs = models.TextField()
    grade = models.TextField()