from django.contrib.auth.decorators import login_required 
from .models import TourPackage
from .forms import TourPackageForm
from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect

class TourListView(ListView):
    model = TourPackage
    template_name = "tours/tour_list.html"
    context_object_name = "tours"

    def get_queryset(self):
        today = timezone.now().date()
        return TourPackage.objects.filter(is_approved=True, expiry_date__gte=today)

def tour_detail(request, tour_id):
    tour = get_object_or_404(TourPackage, id=tour_id, is_approved=True)
    return render(request, "tours/tour_detail.html", {"tour": tour})

def home(request):
    today = timezone.now().date()
    tours = TourPackage.objects.filter(is_approved=True, expiry_date__gte=today)
    return render(request, "tours/home.html", {"tours": tours})

def explore_tours(request):
    today = timezone.now().date()
    tours = TourPackage.objects.filter(is_approved=True, expiry_date__gte=today)
    return render(request, 'tours/explore.html', {'tours': tours})

@login_required
def tour_list(request):
    if request.user.user_type != 'vendor':
        return redirect('unauthorized')  # Optionally add unauthorized.html
    tours = TourPackage.objects.filter(vendor=request.user)
    return render(request, 'tours/tour_list.html', {'tours': tours})
