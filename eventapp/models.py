from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):


    img = models.ImageField(upload_to='img')
    name=models.CharField(max_length=50)
    description=models.TextField()
    location=models.CharField(max_length=100)
    event_date=models.DateField()
    event_time=models.TimeField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    customer_name=models.CharField(max_length=55)
    phone_number=models.CharField(max_length=12)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)


class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=15, blank=True)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    submitted_on=models.DateField(auto_now=True)


    def __str__(self):
        return self.name


class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"