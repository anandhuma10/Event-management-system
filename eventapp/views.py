from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event,Booking, Review
from . forms import BookingForm,ContactForm,ReviewForm

# Create your views here.
   
def index(request):
    events = Event.objects.all()[:3]   # featured events
    reviews = Review.objects.select_related("event", "user").order_by("-created_at")[:6]

    return render(request, "index.html", {
        "events": events,
        "reviews": reviews,
    })


@login_required(login_url='login')
def events(request):
    events = Event.objects.all()

    return render(request, "events.html", {
        "events": events,
    })

    

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
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('/')

    else:
        form = BookingForm()

    return render(request, 'booking.html', {
        'form': form
    })


@login_required(login_url='login')
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)

    return render(request, "event_detail.html", {
        "event": event,
    })

@login_required(login_url='login')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'my_bookings.html', {
        'bookings': bookings
    })





@login_required(login_url='login')
def add_review(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    review = Review.objects.filter(
        event=event,
        user=request.user
    ).first()

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.event = event
            review.save()

            messages.success(request, "Your review has been saved.")
            return redirect("event_detail", id=event.id)

    else:
        form = ReviewForm(instance=review)

    return render(request, "review_form.html", {
        "form": form,
        "event": event,
    })