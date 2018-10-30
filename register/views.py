from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django import HttpResponse

from .models import Register


# Create your views here.

   
