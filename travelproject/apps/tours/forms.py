# apps/tours/forms.py
from django import forms
from .models import TourPackage

class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = ['title', 'description', 'price', 'currency', 'duration', 'category', 'available_spots', 'expiry_date']

    expiry_date = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Ensures the format is YYYY-MM-DD
        widget=forms.DateInput(attrs={'type': 'date'})  # This renders a date picker
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({'placeholder': 'Enter price'})
