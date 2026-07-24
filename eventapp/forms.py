from django import forms 
from.models import Booking,contact

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'