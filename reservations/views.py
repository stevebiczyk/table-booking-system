from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from datetime import date
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Reservation, Table
from .forms import ReservationForm, ContactForm, CustomUserCreationForm


@login_required
def create_booking(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            # Get the table_id value from the POST data
            table_id = request.POST.get('table')
            if table_id:
                reservation.table_id = table_id

            reservation.save()
            return redirect(reverse('booking_confirmation', args=[reservation.id]))
    else:
        initial_data = {}
        if 'table' in request.GET:
            initial_data['table'] = request.GET.get('table')
        if 'date' in request.GET:
            initial_data['date'] = request.GET.get('date')

        reservation_form = ReservationForm(initial=initial_data)

    return render(request, 'booking.html', {'reservation_form': reservation_form})


def booking_confirmation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'booking_confirmation.html', {'reservation': reservation})


def bookings_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'bookings_list.html', {'reservations': reservations})


@login_required
def update_booking(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    # Only the customer who made the booking or the site admin can update the booking
    if request.user != reservation.user and not request.user.is_superuser:
        messages.error(
            request, 'You do not have permission to edit this booking')
        return redirect('bookings_list')
        # raise PermissionDenied

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation', reservation_id=reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'update_booking.html', {'reservation': reservation, 'form': form})


@login_required
def delete_booking(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    # Only the customer who made the booking or the site admin can update the booking
    if request.user != reservation.user and not request.user.is_superuser:
        messages.error(
            request, 'You do not have permission to delete this booking')
        return redirect('bookings_list')
        # raise PermissionDenied

    if request.method == 'POST':
        reservation.delete()
        # Redirect to the bookings list view after successful deletion
        return redirect('bookings_list')

    return render(request, 'delete_booking.html', {'reservation': reservation})


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    menu = [
        ('Starters', [
            {'name': 'Goulash Soup', 'image': 'img/goulash-soup.jpg'},
            {'name': 'Stuffed Peppers', 'image': 'img/stuffed-peppers.jpg'},
            {'name': 'Ujházi Chicken Soup', 'image': 'img/ujhazi-chicken-soup.jpg'},
        ]),
        ('Main Courses', [
            {'name': 'Chicken Paprikash', 'image': 'img/chicken-paprikash.jpg'},
            {'name': 'Töltött Káposzta (Stuffed Cabbage Rolls)',
             'image': 'img/stuffed-cabbage-rolls.jpg'},
            {'name': 'Pörkölt (Beef and Onion Stew)',
             'image': 'img/beef-onion-stew.jpg'},
            {'name': 'Grilled Sausages with Pickles',
                'image': 'img/grilled-sausages.jpg'},
            {'name': 'Hortobágyi Palacsinta (Savory Stuffed Pancakes)',
             'image': 'img/savory-stuffed-pancakes.jpg'},
        ]),
        ('Desserts', [
            {'name': 'Chimney Cake (Kürtőskalács)',
             'image': 'img/chimney-cake.jpg'},
            {'name': 'Somlói Galuska (Trifle)',
             'image': 'img/somloi-galuska.jpg'},
            {'name': 'Strudel (Rétes) with Various Fillings',
             'image': 'img/strudel.jpg'},
        ]),
    ]
    return render(request, 'menu.html', {'menu': menu})


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def gallery(request):
    return render(request, 'gallery.html')


# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             Customer.objects.create(
#                 user=user,
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 email=form.cleaned_data['email'],
#                 phone=form.cleaned_data['phone']
#             )
#             login(request, user)
#             return redirect('home')  # or any other view you want to redirect to after successful registration
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'signup.html', {'form': form})
