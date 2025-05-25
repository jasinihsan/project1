from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.tours.models import TourPackage
from apps.tours.forms import TourPackageForm

def vendor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != "vendor":
            return redirect("home")  # Redirect non-vendors to home or wherever
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
@vendor_required
def vendor_dashboard(request):
    context = {
        'tours': TourPackage.objects.filter(vendor=request.user).order_by('-created_at'),
        'total_tours': TourPackage.objects.filter(vendor=request.user).count(),
        'approved_tours': TourPackage.objects.filter(vendor=request.user, is_approved=True).count(),
        'pending_tours': TourPackage.objects.filter(vendor=request.user, is_approved=False).count(),
    }
    return render(request, 'vendors/vendor_dashboard.html', context)

@login_required
@vendor_required
def add_tour(request):
    if request.method == "POST":
        print("🚨 POST received")  # Debug print
        form = TourPackageForm(request.POST, request.FILES)
        if form.is_valid():
            print("✅ Form is valid")  # Debug print
            tour = form.save(commit=False)
            tour.vendor = request.user
            tour.save()
            messages.success(request, "Tour package added successfully.")
            return redirect("vendors:vendor_dashboard")
        else:
            print("❌ Form is NOT valid")  # Debug print
            print(form.errors)  # Print the actual form errors in terminal
    else:
        form = TourPackageForm()
    return render(request, "vendors/add_tour.html", {"form": form})


@login_required
@vendor_required
def edit_tour(request, tour_id):
    tour = get_object_or_404(TourPackage, id=tour_id, vendor=request.user)
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tour package updated successfully.')
            return redirect('vendors:vendor_dashboard')
    else:
        form = TourPackageForm(instance=tour)
    return render(request, 'vendors/edit_tour.html', {'form': form})

@login_required
@vendor_required
def delete_tour(request, tour_id):
    tour = get_object_or_404(TourPackage, id=tour_id, vendor=request.user)
    tour.delete()
    messages.success(request, 'Tour package deleted successfully.')
    return redirect("vendors:vendor_dashboard")
