from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm
from .models import TravelOption, Booking
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm

def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            login(request, user)    
            return redirect('profile')  
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_profile(request):
    """Handle user profile updates."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

def travel_list(request):
    """Display a list of travel options."""
    travels = TravelOption.objects.all()
    travel_type = request.GET.get('type')
    if travel_type:
        travels = travels.filter(type=travel_type)
    return render(request, 'travel_list.html', {'travels': travels})

def book_travel(request, travel_id):
    print(f'Attempting to book travel with ID: {travel_id}')
    travel_option = get_object_or_404(TravelOption, pk=travel_id)
    print(f'Found travel option: {travel_option}')

    if request.method == 'POST':
        try:
            num_seats = int(request.POST.get('number_of_seats', 0))
            if num_seats <= 0:
                raise ValueError("Number of seats must be greater than zero")
            if travel_option.available_seats >= num_seats:
                Booking.objects.create(
                    user=request.user,
                    travel_option=travel_option,
                    number_of_seats=num_seats,
                    total_price=travel_option.price * num_seats,
                    status='Confirmed'
                )
                travel_option.available_seats -= num_seats
                travel_option.save()
                messages.success(request, 'Booking confirmed!')
                return redirect('my_bookings')
            else:
                messages.error(request, 'Not enough seats available.')
        except ValueError as e:
            messages.error(request, str(e))
    
    return render(request, 'book_travel.html', {'travel': travel_option})

@login_required
def my_bookings(request):
    """Display a list of the user's bookings."""
    try:
        bookings = Booking.objects.filter(user=request.user)
    except Exception as e:

        messages.error(request, f"An error occurred: {e}")
        return redirect('login') 
    return render(request, 'my_bookings.html', {'bookings': bookings})

def cancel_booking(request, booking_id):
    """Cancel a booking."""
    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.status != 'Cancelled':
        booking.status = 'Cancelled'
        booking.save()
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.info(request, 'Booking is already cancelled.')
    return redirect('my_bookings')

def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})

# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         # Handle the form submission here
#         pass
#     return render(request, 'edit_profile.html')