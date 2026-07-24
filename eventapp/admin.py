from django.contrib import admin
from .models import Event,Booking,contact

# Register your models here.

admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(contact)
