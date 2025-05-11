from django.contrib import admin
from .models import TourPackage

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor', 'category', 'price', 'currency', 'duration', 'available_spots','expiry_date')
    list_filter = ('category', 'currency', 'expiry_date')
    search_fields = ('title', 'vendor__email', 'category')

    def has_add_permission(self, request):
        """Only allow vendors to add tours"""
        return request.user.is_authenticated and request.user.user_type == 'vendor'
