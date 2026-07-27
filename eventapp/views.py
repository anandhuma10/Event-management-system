from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from . forms import BookingForm,ContactForm

# Create your views here.
   
def index(request):
    return render(request, "index.html")

@login_required(login_url='login')
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # or a success page
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    form=BookingForm()
    dict_form={
        'form':form
    }


    return render(request, 'booking.html',dict_form)


@login_required(login_url='login')
def event_detail(request,id):
    event = get_object_or_404(Event, id=id)
    return render(request, "event_detail.html", {"event": event})


