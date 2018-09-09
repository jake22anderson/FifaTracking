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
