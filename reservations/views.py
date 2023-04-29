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

    return render(request, 'booking.html',
                  {'reservation_form': reservation_form})


def booking_confirmation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'booking_confirmation.html',
                  {'reservation': reservation})


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
            {'name': 'Goulash Soup', 'price': '$5.50'},
            {'name': 'Stuffed Peppers', 'price': '$6.00'},
            {'name': 'Ujházi Chicken Soup', 'price': '$5.00'},
            {'name': 'Hungarian Bruschetta', 'price': '$4.50'},
            {'name': 'Cucumber Salad', 'price': '$3.50'},
        ]),
        ('Main Courses', [
            {'name': 'Chicken Paprikash', 'price': '$11.50'},
            {'name': 'Töltött Káposzta (Stuffed Cabbage Rolls)',
             'price': '$12.00'},
            {'name': 'Pörkölt (Beef and Onion Stew)', 'price': '$13.00'},
            {'name': 'Grilled Sausages with Pickles', 'price': '$10.00'},
            {'name': 'Hortobágyi Palacsinta (Savory Stuffed Pancakes)',
             'price': '$10.50'},
            {'name': 'Hungarian Beef Goulash', 'price': '$14.00'},
            {'name': 'Hungarian Meatballs', 'price': '$11.00'},
        ]),
        ('Desserts', [
            {'name': 'Chimney Cake (Kürtőskalács)', 'price': '$7.00'},
            {'name': 'Somlói Galuska (Trifle)', 'price': '$7.50'},
            {'name': 'Strudel (Rétes) with Various Fillings',
             'price': '$6.50'},
            {'name': 'Hungarian Crepes (Palacsinta)', 'price': '$7.00'},
            {'name': 'Dobos Torte', 'price': '$8.00'},
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
