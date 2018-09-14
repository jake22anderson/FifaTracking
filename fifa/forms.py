from django import forms
from .models import *
from . import views



class PlayerForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)

class MatchForm(forms.Form):
    def __init__(self,data,*args,**kwargs):
        super(MatchForm,self).__init__(*args, **kwargs)
        self.fields['player1']=forms.ChoiceField(label = "Player1",choices = data['choices'] , widget = forms.Select(), required = False)
        self.fields['player2']=forms.ChoiceField(label = "Player2",choices = data['choices'],  widget = forms.Select(), required = False)
        self.fields['p1score'] = forms.IntegerField();
        self.fields['p2score'] = forms.IntegerField();
