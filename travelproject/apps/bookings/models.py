from django.db import models
from django.conf import settings
from apps.tours.models import TourPackage
from decimal import Decimal, InvalidOperation


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    num_people = models.PositiveIntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # ✅ added

    def __str__(self):
        return f"{self.user.email} - {self.tour.title}"
