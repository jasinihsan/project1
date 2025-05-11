from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.vendors.models import TourPackage  
from apps.vendors.forms import TourPackageForm 

def vendor_required(view_func):
    """ Custom decorator to ensure only vendors can access views """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != "vendor":
            return redirect("home")  
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
@vendor_required
def vendor_dashboard(request):
    tours = TourPackage.objects.filter(vendor=request.user)
    return render(request, "vendors/vendor_dashboard.html", {"tours": tours})

@login_required
@vendor_required
def add_tour(request):
    if request.method == "POST":
        form = TourPackageForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.vendor = request.user
            tour.save()
            return redirect("vendors:vendor_dashboard")
    else:
        form = TourPackageForm()
    return render(request, "vendors/add_tour.html", {"form": form})

@login_required
@vendor_required
def edit_tour(request, tour_id):
    tour = get_object_or_404(TourPackage, id=tour_id, vendor=request.user)
    if request.method == "POST":
        form = TourPackageForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect("vendors:vendor_dashboard")
    else:
        form = TourPackageForm(instance=tour)
    return render(request, "vendors/edit_tour.html", {"form": form})

@login_required
@vendor_required
def delete_tour(request, tour_id):
    tour = get_object_or_404(TourPackage, id=tour_id, vendor=request.user)
    tour.delete()
    return redirect("vendors:vendor_dashboard")
