
from django.urls import path
from django.shortcuts import render
from .views import booking_home, book_tour, vendor_bookings, vendor_home, user_bookings

app_name = "bookings"

urlpatterns = [
    path("", booking_home, name="booking_home"),
    path("vendor/bookings/", vendor_bookings, name="vendor_bookings"),
    path("vendor/home/", vendor_home, name="vendor_home"),
    path("success/", lambda request: render(request, "bookings/booking_success.html"), name="booking_success"), 
    path("my-bookings/", user_bookings, name="user_bookings"),  
    path("book-tour/<int:tour_id>/", book_tour, name="book_tour"),
]
