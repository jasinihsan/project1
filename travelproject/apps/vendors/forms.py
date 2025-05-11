from django import forms
from .models import TourPackage

class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = ["title", "description", "price", "location", "duration", "is_active"]
