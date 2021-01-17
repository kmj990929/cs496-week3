from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.TextField()
    userID = models.TextField()
    userPW = models.TextField()
    mbti = models.TextField()