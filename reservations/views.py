from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from datetime import date
from django.urls import reverse
from .models import Customer, Reservation, Table
from .forms import ReservationForm, CustomerForm


def create_booking(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if reservation_form.is_valid() and customer_form.is_valid():
            customer = customer_form.save()
            reservation = reservation_form.save(commit=False)
            reservation.customer = customer
            reservation.save()
            return redirect('bookings_list')
    else:
        reservation_form = ReservationForm()
        customer_form = CustomerForm()

        if 'table' in request.GET:
            table_id = request.GET.get('table')
            table = Table.objects.get(id=table_id)
            reservation_form.update_time_choices(table)

    return render(request, 'booking.html', {'reservation_form': reservation_form, 'customer_form': customer_form})


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


# def booking(request):
#     return render(request, 'booking.html')
