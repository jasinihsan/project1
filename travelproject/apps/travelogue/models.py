from django.db import models

class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")
    image = models.ImageField(upload_to='package_images/')
    available_slots = models.IntegerField(default=10)

    def __str__(self):
        return self.title

# Create your models here.
