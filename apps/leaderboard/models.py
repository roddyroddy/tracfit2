from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    admin = models.IntegerField(default = 0)
    rank = models.IntegerField(default = 0)
    rank_amrap = models.IntegerField(default = 0)

class Wod(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, related_name = "Wods")
    style = models.CharField(max_length=50)

class Score(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    amrap_score = models.IntegerField()
    string = models.CharField(max_length = 30)
    timed_score = models.IntegerField()
    wod = models.ForeignKey(Wod, related_name = "wods_score")
    user = models.ForeignKey(User, related_name = "user_score")
