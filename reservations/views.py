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
