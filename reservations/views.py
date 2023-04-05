from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import generic
from .forms import ReservationForm


def booking(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            customer, _ = Customer.objects.get_or_create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
            )
            reservation.customer = customer
            reservation.save()
            # Redirect to a success page or show a success message
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


def booking(request):
    return render(request, 'booking.html')
