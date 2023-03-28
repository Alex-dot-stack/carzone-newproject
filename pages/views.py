from django.shortcuts import render
from .models import Teams
from cars.models import Cars

# Create your views here.

def home(request):
    # fetch all data inside Teams-Model
    teams = Teams.objects.all()
    # fetch all featured Cars
    featured_cars = Cars.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Cars.objects.order_by('-created_date')
    # hier legen wir fest, was wir nach außen für das HTML Template transportieren möchten, damit wir von HTML aus zugreifen können
    data = {
        'teams':teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
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