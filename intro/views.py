from django.shortcuts import render,redirect
from django.contrib import auth

# Create your views here.
def intro(request):
    return render(request, 'intro/intro.html')

