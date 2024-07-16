from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
