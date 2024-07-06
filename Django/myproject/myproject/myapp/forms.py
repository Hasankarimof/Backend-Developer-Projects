from django import forms
from .models import Booking,Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'guest_count', 'reservation_time', 'comments']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'attachment']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


