from django import forms
from .models import Reservation
from .models import Staff


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'date', 'time',
                  'number_of_guests', 'special_requests']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name']
