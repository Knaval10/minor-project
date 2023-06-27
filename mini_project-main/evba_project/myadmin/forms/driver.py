from tracker.models import *
from django import forms



class DriverAddForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('fname','lname','gender','birth_date','email','contact_no','avatar','liscence_no','address','latitude','longitude','password')
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Enter Gender'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Addres'}),
            'avatar':forms.FileInput(attrs={'class':'form-control','placeholder':'select file'}),
            'liscence_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Liscence No'}),
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

class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('fname','lname','gender','birth_date','email','contact_no','avatar','liscence_no','address','latitude','longitude','status','online','active')
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Enter Gender'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Addres'}),
            'avatar':forms.FileInput(attrs={'class':'form-control','placeholder':'select file'}),
            'liscence_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Liscence No'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact Number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'latitude':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter latitude'}),
            'longitude':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter longitude'}),
            # 'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter password'}),
        
            'status':forms.Select(attrs={'class':'form-select'}),
            'online':forms.CheckboxInput,
            'active':forms.CheckboxInput,
            

        }
        labels = {
            'fname':'First Name',
            'lname':'Last Name'
        }


