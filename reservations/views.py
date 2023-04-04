from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import generic
from .forms import ReservationForm


def booking(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = ReservationForm()
    return render(request, 'booking_form.html', {'form': form})


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


def booking(request):
    return render(request, 'booking.html')
