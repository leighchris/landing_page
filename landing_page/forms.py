from django import forms
from django.core import validators
from register.models import Register
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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
        
class SignupForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ("username", 
                  "first_name", 
                  "last_name", 
                  "email", 
                  "password1",
                  "password2",
                 )
    def save(self, commit=True):
        cleaned_data= super().clean()
        user = super(SignupForm, self).save(commit=False)
        user.first_name = cleaned_data['first_name']
        user.last_name = cleaned_data['last_name']
        user.email = cleaned_data['email']
        
        if commit:
            user.save()
            
        return user
    
class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )
        

        
