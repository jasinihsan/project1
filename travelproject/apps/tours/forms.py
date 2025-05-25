from django import forms
from .models import TourPackage

class TourPackageForm(forms.ModelForm):
    expiry_date = forms.DateField(
        input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = TourPackage
        fields = ['title', 'description', 'price', 'currency', 'duration', 'category', 'available_spots', 'expiry_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({'placeholder': 'Enter price'})
