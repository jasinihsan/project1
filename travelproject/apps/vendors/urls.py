from django.urls import path
from . import views

app_name = "vendors" 

urlpatterns = [
    path("", views.vendor_dashboard, name="vendor_dashboard"),
    path("dashboard/", views.vendor_dashboard, name="dashboard"),
    path("add-tour/", views.add_tour, name="add_tour"),
    path("edit-tour/<int:tour_id>/", views.edit_tour, name="edit_tour"),
    path("delete-tour/<int:tour_id>/", views.delete_tour, name="delete_tour"),
]
