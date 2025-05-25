from django.urls import path
from .views import TourListView, tour_detail, home, explore_tours , tour_list
from . import views

app_name = "tours"

urlpatterns = [
    path("", home, name="home"),
    path("list/", TourListView.as_view(), name="tour_list"),
    path("tour/<int:tour_id>/", tour_detail, name="tour_detail"),
    path("explore/", explore_tours, name="explore_tours"),
    path("my-tours/", tour_list, name="my_tours"), 

    
    
]