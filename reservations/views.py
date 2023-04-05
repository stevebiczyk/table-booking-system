from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import generic
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
    return render(request, 'booking.html', {'form': form})


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
