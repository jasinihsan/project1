from django.urls import path
from .views import TourListView, tour_detail , home 
from . import views  

app_name = "tours"

urlpatterns = [
    path("", home, name="home"), 
    path("list/", TourListView.as_view(), name="tour_list"),  
    path("<int:tour_id>/", tour_detail, name="tour_detail"),
    path('explore/', views.explore_tours, name='tours_list'),
    path("add/",views.add_tour, name="add_tour"),
   
]

