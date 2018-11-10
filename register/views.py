
# Create your views here.


from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from register.models import Register
from register.utils import SendSubscribeMail
from . import forms
from .forms import SignupForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


#def subscribe(request):
#    if request.method == 'POST':
#        email = request.POST['email']
#        email_qs = Subscribe.objects.filter(email = email)
#        if email_qs.exists():
#            data = {"status" : "404"}
#            return JsonResponse(data)
#        else:
#            Subscribe.objects.create(email = email)
#            SendSubscribeMail(email) # Send the Mail, Class available in utils.py
#    return HttpResponse("/")
#



class HomeView(TemplateView):
    template_name = 'home.html'
    
    
    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})


def homeform_view(request):
    form = forms.HomeForm()
    first_name = ''
    last_name = ''
    email = ''
    if request.method == 'POST':
        form = forms.HomeForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            form = forms.HomeForm()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'home.html', {'form': form})






   
