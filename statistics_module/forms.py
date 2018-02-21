from django import forms
from statistics_module.choices import *

class SearchingForm(forms.Form):
    year = forms.CharField()
    month = forms.ChoiceField(choices=MONTH_CHOICES)