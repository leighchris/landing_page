from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from register.models import Register
from .forms import HomeForm, SignupForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm


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
    form = HomeForm()
    first_name = ''
    last_name = ''
    email = ''
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            form = HomeForm()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'home.html', {'form': form})

def signup_view(request):
    form = SignupForm()
    if request.method =='POST':
        form= SignupForm(request.POST or None)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('signup'))
    return render(request, 'signup.html', {'form': form})


def profile_view(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)

def edit_profile(request):
    form = EditProfileForm()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance =request.user)
        if form.is_valid():
            form.save() 
        return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditProfileForm(instance = request.user)
        return render(request, 'edit_profile.html', {'form': form})




