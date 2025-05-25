from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.account_home, name="account_home"),
    path("register/", views.register_view, name="register"),  
    path('login/', views.login_view, name='login'),
    path("logout/", views.user_logout, name="user_logout"),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
]
