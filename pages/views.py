from django.shortcuts import render
from .models import Teams

# Create your views here.

def home(request):
    # fetch all data inside Teams-Model
    teams = Teams.objects.all()
    data = {
        'teams':teams,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Teams.objects.all()
    data = {
        'teams':teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')