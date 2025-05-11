from django.shortcuts import render, get_object_or_404  
from .models import TourPackage
from django.http import HttpResponse

def home(request):
    packages = TourPackage.objects.all()
    return render(request, 'travelogue/home.html', {'packages': packages})  

def tour_detail(request, tour_id):
    tour = get_object_or_404(TourPackage, id=tour_id)
    return render(request, 'travelogue/tour_detail.html', {'tour': tour})  
