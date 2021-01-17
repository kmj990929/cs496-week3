from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.TextField()
    userPW = models.TextField()
    mbti = models.TextField()