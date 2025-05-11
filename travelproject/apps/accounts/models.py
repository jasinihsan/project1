from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager  

class CustomUser(AbstractUser):
    username = None  
    full_name = models.CharField(max_length=255, default='', blank=True)
    email = models.EmailField(unique=True)
    
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['full_name', 'user_type']

    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
