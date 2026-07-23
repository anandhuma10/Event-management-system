from django.shortcuts import render
from .models import Event

# Create your views here.
   
def index(request):
    return render(request, "index.html")

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')
