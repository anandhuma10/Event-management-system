from django import forms 
from.models import Booking,contact,Review

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ["user", "booked_on"]

        widgets = {
            "customer_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name",
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number",
            }),
            "event": forms.Select(attrs={
                "class": "form-select",
            }),
            "booking_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
            }),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        exclude = ["submitted_on"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email address",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the subject",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your message here...",
            }),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]

        widgets = {
            "rating": forms.Select(
                choices=[
                    ("", "Select Rating"),
                    (1, "⭐ 1 - Poor"),
                    (2, "⭐⭐ 2 - Fair"),
                    (3, "⭐⭐⭐ 3 - Good"),
                    (4, "⭐⭐⭐⭐ 4 - Very Good"),
                    (5, "⭐⭐⭐⭐⭐ 5 - Excellent"),
                ],
                attrs={
                    "class": "form-select",
                },
            ),
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Tell us about your experience with this event...",
                },
            ),
        }

        labels = {
            "rating": "Your Rating",
            "comment": "Your Review",
        }