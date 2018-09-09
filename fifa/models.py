from __future__ import unicode_literals

from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length =100)
    def __str__(self):
        return self.first_name

class League(models.Model):
    player = models.ForeignKey('Player',on_delete = models.CASCADE)
