from django import forms
from .models import *
from . import views



class PlayerForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)

class MatchForm(forms.Form):
    def __init__(self,user,*args,**kwargs):
        super(waypointFrom,self).__init__(*args, **kwargs)
        self.fields['player1']=forms.ChoiceField(label = "Player1",choices = data['choices'] , widget = forms.Select(), required = True)
        self.fields['player2']=forms.ChoiceField(label = "Player2",choices = data['choices'],  widget = forms.Select(), required = True)
        self.fields['p1score'] = forms.IntegerField();
        self.fields['p2score'] = forms.IntegerField();
    def __init__(self, *args, **kwargs):
            # Get 'initial' argument if any
            initial_arguments = kwargs.get('initial', None)
            updated_initial = {}
            if initial_arguments:
                  # We have initial arguments, fetch 'user' placeholder variable if any
                  user = initial_arguments.get('user',None)
                  # Now update the form's initial values if user
                  if user:
                        updated_initial['name'] = getattr(user, 'first_name', None)
                        updated_initial['email'] = getattr(user, 'email', None)
            # You can also initialize form fields with hardcoded values
            # or perform complex DB logic here to then perform initialization
            updated_initial['comment'] = 'Please provide a comment'
            # Finally update the kwargs initial reference
            kwargs.update(initial=updated_initial)
            super(ContactForm, self).__init__(*args, **kwargs)
