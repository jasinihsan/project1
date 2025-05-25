from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from apps.accounts.forms import RegisterForm, CustomUserEditForm, LoginForm
from apps.accounts.models import CustomUser
from apps.tours.models import TourPackage
from django.urls import reverse



def register_view(request):
    """Handles User Registration."""
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.full_name = form.cleaned_data.get('full_name')
            user.set_password(form.cleaned_data['password'])
           
            user.save()  

            login(request, user)  
            messages.success(request, "Registration successful!")

            return redirect("accounts:user_dashboard")

        else:
            print("Form Errors:", form.errors)  

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    """Handles User Login."""
    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("username").strip().lower()
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=email, password=password)  

            if user:
                login(request, user)
                messages.success(request, "Login successful!")

               
                if user.user_type == "customer":
                    return redirect(reverse("accounts:user_dashboard"))
                elif user.user_type == "vendor":
                    return redirect(reverse("vendors:vendor_dashboard"))
                else:
                    return redirect(reverse("admin:index")) 
            messages.error(request, "Invalid email or password.")

        else:
            print("Form Errors:", form.errors) 
    return render(request, "accounts/login.html", {"form": form})


@login_required

def user_dashboard(request):
    if request.user.user_type == 'customer':
        return render(request, 'accounts/customer_dashboard.html')
    else:
        return render(request, 'vendors/vendor_dashboard.html')  

@login_required
def vendor_dashboard(request):
    """Vendor Dashboard."""
    if request.user.user_type == 'vendor':
        # Only show tours belonging to the logged-in vendor
        tours = TourPackage.objects.filter(vendor=request.user)
        return render(request, "vendors/vendor_dashboard.html", {'tours': tours})
    else:
        messages.error(request, "you are not authorized to view this page .")
        return redirect("accounts:user_dashboard")



def user_logout(request):
    """Logs out the user and redirects to login."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse("accounts:login"))  


@login_required
def edit_profile(request):
    """Allows only customers to edit their profile."""
    if request.user.user_type != 'customer':
        messages.error(request, "You are not authorized to edit profile.")
        return redirect("accounts:login")

    user = request.user
    form = CustomUserEditForm(request.POST or None, instance=user)

    if request.method == "POST" and form.is_valid():
        updated_user = form.save(commit=False)
        updated_user.user_type = user.user_type 
        
        
        new_password = form.cleaned_data.get('password')
        if new_password:
            updated_user.set_password(new_password)
        updated_user.save()

        messages.success(request, "Profile updated successfully!")
        
        if new_password:
            login(request, updated_user)
            
        return redirect("accounts:user_dashboard")

    return render(request, "accounts/edit_profile.html", {"form": form})


def account_home(request):
    """Homepage for account-related features."""
    return render(request, "accounts/account_home.html")


def custom_login(request):
    """Handles user login."""
    form = LoginForm(request.POST or None)  

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['username'].strip().lower()
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")

                if user.user_type == "customer":
                    return redirect('accounts:user_dashboard')
                elif user.user_type == "vendor":
                    return redirect('vendors:vendor_dashboard')
                else:
                    return redirect('admin:index')  
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Please correct the errors in the form")

    return render(request, 'accounts/login.html', {'form': form})
