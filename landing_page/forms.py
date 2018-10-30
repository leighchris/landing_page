from django import forms
from django.core import validators
from register.models import Register
from django.forms import ModelForm


def must_be_empty(value):
    if value:
        raise forms.ValidationError("Is not empty")

class HomeForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    honeypot = forms.CharField(required=False, 
                               widget= forms.HiddenInput, 
                               label="Leave Empty", 
                               validators=[must_be_empty],
                              )
    class Meta:
        model = Register
        fields = ("first_name", "last_name", "email" ,)
        
def clean(self):
    cleaned_data = super().clean()
    first_name = cleaned_data.get('first_name')
    last_name = cleaned_data.get('last_name')
    email = cleaned_data.get('email')
    
