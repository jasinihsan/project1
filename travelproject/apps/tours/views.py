from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from .models import TourPackage
from .forms import TourPackageForm
from django.utils import timezone


class TourListView(ListView):
    model = TourPackage
    template_name = "tours/tour_list.html"
    context_object_name = "tours"

def tour_detail(request, tour_id):
    """Show details of a specific tour package."""
    tour = get_object_or_404(TourPackage, id=tour_id)
    return render(request, "tours/tour_detail.html", {"tour": tour})

def home(request):
    """Homepage showing all tours."""
    tours = TourPackage.objects.all()  
    return render(request, "tours/home.html", {"tours": tours})

def explore_tours(request):
    today = timezone.now().date()  
    tours = TourPackage.objects.filter(expiry_date__gte=today)  
    return render(request, 'tours/explore.html', {'tours': tours})

@login_required
def add_tour(request):
    if request.method == 'POST':
        form = TourPackageForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.vendor = request.user
            tour.save()
            return redirect('tours:tour_list')  
    else:
        form = TourPackageForm()

    return render(request, "tours/add_tour.html", {"form": form})
