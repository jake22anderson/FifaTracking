from __future__ import unicode_literals

from django.db import models




class League(models.Model):
    league_name = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.league_name

class Match(models.Model):
    player1 = models.ForeignKey('Player', on_delete = models.CASCADE, related_name = "player2")
    player2 = models.ForeignKey('Player', on_delete = models.CASCADE, related_name = "player1" )
    p1score = models.IntegerField()
    p2score = models.IntegerField()
    league =  models.ForeignKey('League', on_delete = models.CASCADE)

class Player(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name  = models.CharField(max_length = 100)
    league = models.ForeignKey('League', on_delete = models.CASCADE)
    def __str__(self):
        return self.first_name
