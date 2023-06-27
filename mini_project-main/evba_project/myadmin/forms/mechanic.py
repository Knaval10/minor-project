from tracker.models import *
from django import forms



class MechanicAddForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=VehicleService.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Mechanic
        fields = ('fname','lname','gender','birth_date','email','contact_no','avatar','pan_no','address','latitude','longitude','password','services')
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Enter Gender'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Addres'}),
            'avatar':forms.FileInput(attrs={'class':'form-control','placeholder':'select file'}),
            'pan_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Liscence No'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact Number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'latitude':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter latitude'}),
            'longitude':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter longitude'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter password'}),
            

        }
        labels = {
            'fname':'First Name',
            'lname':'Last Name'
        }


class MechanicUpdateForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=VehicleService.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Mechanic
        fields = ('fname','lname','gender','birth_date','email','contact_no','avatar','pan_no','address','latitude','longitude','status','services','online','active')
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Enter Gender'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Addres'}),
            'avatar':forms.FileInput(attrs={'class':'form-control','placeholder':'select file'}),
            'pan_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Liscence No'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact Number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'latitude':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter latitude'}),
            'longitude':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter longitude'}),
            'online':forms.CheckboxInput,
            'active':forms.CheckboxInput,

            # 'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter password'}),
        
            'status':forms.Select(attrs={'class':'form-select'})
            

        }
        labels = {
            'fname':'First Name',
            'lname':'Last Name'
        }