from django import forms
from tracker.models import *


class ServiceForm(forms.ModelForm):
    class Meta:
        model = VehicleService
        fields = ('name','image')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter vehicle service name'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }
    