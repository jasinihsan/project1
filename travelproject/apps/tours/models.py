from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TourPackage(models.Model):
    CATEGORY_CHOICES = [
        ('adventure', 'Adventure'),
        ('beach', 'Beach'),
        ('cultural', 'Cultural'),
        ('wildlife', 'Wildlife'),
        ('mountain', 'Mountain'),
        ('historical', 'Historical'),
    ]
    
    CURRENCY_CHOICES = [
        ('USD', ' ($)'),
        ('INR', ' (₹)'),
        ('EUR', ' (€)'),
        ('GBP', ' (£)'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='INR')
    duration = models.PositiveIntegerField(help_text="Duration in days")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    available_spots = models.PositiveIntegerField(default=10)
    expiry_date = models.DateField()
    
    vendor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="tours_tourpackages" 
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    @property
    def is_expired(self):
        return self.expiry_date < timezone.now().date()
    
    def __str__(self):
        return self.title
