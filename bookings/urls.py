
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('travels/', views.travel_list, name='travel_list'), 
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),  
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('bookings/my_bookings/', views.my_bookings, name='my_bookings'),
    
]


