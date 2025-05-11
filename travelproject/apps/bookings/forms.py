from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_people'] 
    num_people = forms.IntegerField(min_value=1, required=True) 
