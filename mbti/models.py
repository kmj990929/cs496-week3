# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Answer(models.Model):
    question_number = models.IntegerField()
    answer = models.IntegerField()

class User(models.Model):
    userID = models.CharField(max_length=200)
    userPW = models.CharField(max_length=200)
    mbti = models.CharField(max_length=200)
