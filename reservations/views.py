from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Reservation
from .forms import ReservationForm


def create_booking(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            customer_data = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
            }
            customer, _ = Customer.objects.get_or_create(**customer_data)
            reservation = form.save(commit=False)
            reservation.customer = customer
            reservation.save()
            return redirect('bookings_list')
    else:
        form = ReservationForm()

        if 'table' in request.GET:
            table_id = request.GET.get('table')
            table = Table.objects.get(id=table_id)
            form.update_time_choices(table)

    return render(request, 'booking.html', {'form': form})


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
