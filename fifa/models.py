from __future__ import unicode_literals

from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name  = models.CharField(max_length = 100)
    league = models.ForeignKey('League', on_delete = models.CASCADE)


class League(models.Model):
    league_name = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.league_name
