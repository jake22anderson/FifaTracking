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
        data =  {'choices':getPlayerListTup(l_id)}
        match_form = MatchForm(data)
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
        playerlist = Player.objects.filter(league = league)
        matchlist = Match.objects.filter(league = league)
        updateAllRecords(league_id)
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
            record = Record(wins = 0, losses = 0)
            record.save()
            player = Player(first_name = fn, last_name = ln, league = league[0], record = record)
            player.save()
        else:
            print("not valid form")

    league_id = kwargs['league_id']
    return HttpResponseRedirect('/league/'+str(league_id)+'/')

def addMatch(request, **kwargs):
    if request.method == 'POST':
        league_id = kwargs['league_id']
        playerlist = getPlayerListTup(league_id)
        player1 = request.POST.get('player1')
        player2 = request.POST.get('player2')
        p1score = request.POST.get('p1score')
        p2score = request.POST.get('p2score')
        p1 = Player.objects.filter(pk = player1)[0]
        p2 = Player.objects.filter(pk = player2)[0]
        league = League.objects.filter(pk = league_id)[0]
        match_obj = Match(player1 = p1, player2 = p2, p1score = int(p1score), p2score =int(p2score), league = league)
        match_obj.save()

    return HttpResponseRedirect('/league/'+str(league_id)+'/')

def getPlayerListTup(league_id):
    PlayerList={}
    for p in Player.objects.filter(league = league_id):
        PlayerList[p.id] = ("%s %s" %(p.first_name,p.last_name))
    playerlisttup = tuple(PlayerList.items())
    return playerlisttup

def updateAllRecords(league_id):
    playerlist = Player.objects.filter(league = league_id)
    for p in playerlist:
        p.record.wins = 0
        p.record.losses = 0
        p.record.save()
    matchlist = Match.objects.filter(league = League.objects.filter(pk = league_id)[0])
    for m in matchlist:
        record1 = m.player1.record
        record2 = m.player2.record
        wins1 = record1.wins
        losses1 = record1.losses
        wins2 = record2.wins
        losses2 = record2.losses
        if m.p1score>m.p2score:
            wins1 = wins1 +1
            losses2 = losses2 +1
            record1.wins = wins1
            record2.losses = losses2
        elif m.p2score>m.p1score:
            wins2 = wins2+1
            losses1 = losses1+1
            record1.losses = losses1
            record2.wins = wins2
        record1.save()
        record2.save()
