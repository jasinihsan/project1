from django.contrib import admin
from .models import TourPackage

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "vendor", "price", "location", "is_active", "created_at")