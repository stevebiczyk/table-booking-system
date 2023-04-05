from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    #  path('booking/', views.booking, name='booking'),
    path('booking/create/', views.create_booking, name='create_booking'),
    #  path('booking/', create_booking, name='booking')
    path('bookings/', views.bookings_list, name='bookings_list'),
    path('booking/update/<int:pk>/', views.update_booking, name='update_booking'),
]
