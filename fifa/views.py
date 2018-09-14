from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from django.template import loader
from .forms import *
from django.views.generic.edit import FormView


class AddPlayer(TemplateView):
    def get(self,request,**kwargs):
        player_form = PlayerForm()
        return render(request,"addplayer.html", {"form":player_form})

class AddMatch(TemplateView):
    def get(self,request, **kwargs):
        l_id= kwargs['league_id']
        PlayerList = {}
        for p in Player.objects.filter(league = request.session['league']):
            PlayerList[p.id] = p.id
        playerlisttup = tuple(PlayerList.items())
        match_form = MatchForm(request.POST, data =  {'choices':playerlisttup})
        return render(request,"addmatch.html", {"form":match_form})
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
        matchlist = Match.objects.filter(league = league_id)
        print(matchlist)
        return render(request, "leaguedashboard.html", {'league':league,'playerlist':playerlist, 'matchlist':matchlist})



class PlayerView(TemplateView):
    def get(self,request,**kwargs):
        player_id = kwargs['player_id']
        player_set = Player.objects.filter(pk = player_id)
        player = player_set[0]
        return render(request, "playerdashboard.html", {'player': player})
class PlayerList(FormView):
    def get():
        PlayerList = {}
        for p in Player.objects.filter(league = request.session['league']):
            PlayerList[p.id] = p.id
        playerlisttup = tuple(PlayerList.items())
        return playerlisttup

def addPlayer(request, **kwargs):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            fn = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            league= League.objects.filter(pk = kwargs['league_id'])
            player = Player(first_name = fn, last_name = ln, league = league[0])
            player.save()
        else:
            print("not valid form")

    league_id = kwargs['league_id']
    return HttpResponseRedirect('/league/'+str(league_id)+'/')

def addMatch(request, **kwargs):
    if request.method == 'POST':
        l_id= kwargs['league_id']
        PlayerList = {}
        for p in Player.objects.filter(league = request.session['league']):
            PlayerList[p.id] = p.id
        playerlisttup = tuple(PlayerList.items())
        form = MatchForm(request.POST)
        if form.is_valid():
            print("WELL HELL FUCKING O")
        else:
            form.add()
    league_id = kwargs['league_id']
    return HttpResponseRedirect('/league/'+str(league_id)+'/')

def getPlayerListTup():

    return playerlisttup
