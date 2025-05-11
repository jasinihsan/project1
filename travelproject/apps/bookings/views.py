from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm  
from apps.tours.models import TourPackage
from apps.payments.models import Payment

@login_required
def book_tour(request, tour_id):
    tour = get_object_or_404(TourPackage, id=tour_id)

    
    if request.user.user_type != 'customer':
        messages.error(request, "You are not allowed to book a tour.")
        return redirect('home')

    form = BookingForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.tour = tour
        booking.num_people = form.cleaned_data.get('num_people', 1)

        
        if tour.price is not None and booking.num_people > 0:
            total_price = booking.num_people * tour.price
        else:
            total_price = 0  

        booking.total_price = total_price  
        booking.save()  

        
        payment = Payment.objects.create(
            user=request.user,
            booking=booking,
            amount=total_price,
            method='cod',  
            status='pending'
        )

    
        return redirect('payments:make_payment', payment_id=payment.id)

    return render(request, "bookings/book_tour.html", {"form": form, "tour": tour})


def booking_home(request):
    return render(request, 'bookings/booking_home.html')

def vendor_bookings(request):
    bookings = Booking.objects.filter(tour__vendor=request.user)
    return render(request, 'bookings/vendor_bookings.html', {'bookings': bookings})

def vendor_home(request):
    tours = TourPackage.objects.filter(vendor=request.user)
    return render(request, 'bookings/vendor_home.html', {'tours': tours})

def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/user_bookings.html', {'bookings': bookings})
