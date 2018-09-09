from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from django.template import loader



class HomepageView(TemplateView):
    def get(self,request,**kwargs):
        LeagueList = League.objects.all()
        context = {'LeagueList':LeagueList}
        return render(request, "homepage.html", context )

class LeagueView(TemplateView):
    def get(self,request, **kwargs):
        league_id = kwargs['league_id']
        league_list = League.objects.filter(pk = league_id)
        league= league_list[0]
        name = league.league_name
        playerlist = Player.objects.filter(league = league_id)
        print(playerlist)
        return render(request, "leaguedashboard.html", {'league':league,'playerlist':playerlist})
class PlayerView(TemplateView):
    def get(self,request,**kwargs):
        player_id = kwargs['player_id']
        player_set = Player.objects.filter(pk = player_id)
        player = player_set[0]
        return render(request, "playerdashboard.html", {'player': player})
