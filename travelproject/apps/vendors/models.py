from django.db import models
from apps.accounts.models import CustomUser  

class TourPackage(models.Model):
    vendor = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name="vendors_tourpackages",  
        limit_choices_to={'user_type': 'vendor'}
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
