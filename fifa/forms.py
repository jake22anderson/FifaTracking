from django import forms
from .models import *

class PlayerForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
