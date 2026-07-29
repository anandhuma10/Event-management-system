from django import forms 
from.models import Booking,contact,Review

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



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(
                choices=[
                    (1, '⭐ 1'),
                    (2, '⭐⭐ 2'),
                    (3, '⭐⭐⭐ 3'),
                    (4, '⭐⭐⭐⭐ 4'),
                    (5, '⭐⭐⭐⭐⭐ 5'),
                ],
                attrs={'class': 'form-select'}
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Share your experience...'
                }
            ),
        }