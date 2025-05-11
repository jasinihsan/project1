from django.urls import path
from . import views

app_name = 'payments'  

urlpatterns = [
    path('make/<int:payment_id>/', views.make_payment, name='make_payment'),
]
