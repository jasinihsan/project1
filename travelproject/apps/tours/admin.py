from django.contrib import admin
from .models import TourPackage

try:
    admin.site.unregister(TourPackage)
except admin.sites.NotRegistered:
    pass

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'vendor', 'category', 'price', 'currency',
        'duration', 'available_spots', 'expiry_date', 'is_approved'
    )
    list_filter = ('category', 'currency', 'expiry_date', 'is_approved')
    search_fields = ('title', 'vendor__email', 'category')
    actions = ['approve_selected_tours']

    def has_add_permission(self, request):
        
        return request.user.is_authenticated and (request.user.is_superuser or request.user.user_type == 'vendor')

    def approve_selected_tours(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} tour(s) successfully approved.")
    approve_selected_tours.short_description = "✅ Approve selected tour packages"
