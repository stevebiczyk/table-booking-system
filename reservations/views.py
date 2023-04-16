from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from datetime import date
from django.urls import reverse
from django.db import IntegrityError
from .models import Customer, Reservation, Table
from .forms import ReservationForm, CustomerForm


def create_booking(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if reservation_form.is_valid() and customer_form.is_valid():
            try:
                customer = customer_form.save()
            except IntegrityError:
                # If the email already exists, retrieve the existing customer
                customer = Customer.objects.get(
                    email=customer_form.cleaned_data['email'])
            reservation = reservation_form.save(commit=False)
            reservation.customer = customer
            # Make sure to get the table_id value from the POST data
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
        customer_form = CustomerForm()

    return render(request, 'booking.html', {'reservation_form': reservation_form, 'customer_form': customer_form})


def booking_confirmation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'booking_confirmation.html', {'reservation': reservation})


def bookings_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'bookings_list.html', {'reservations': reservations})


def update_booking(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'update_booking.html', {'form': form})


def delete_booking(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

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
    return render(request, 'menu.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')
