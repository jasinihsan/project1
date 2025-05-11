from django.contrib import admin
from django.urls import path, include
from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),  
    path("tours/", include("apps.tours.urls")), 
    path('', home, name='home'),  
    path('travelogue/', include('apps.travelogue.urls')),  
    path('bookings/', include('apps.bookings.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('vendors/', include('apps.vendors.urls')),
]
