from django import forms
from .models import Customer, Reservation
from .models import Staff
import datetime


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time',
                  'number_of_guests', 'special_requests']

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget.attrs.update({"class": "time-field"})

    def update_time_choices(self, table):
        reserved_times = Reservation.objects.filter(
            table=table, date=self.cleaned_data['date']).values_list('time', flat=True)
        available_times = []

        for hour in range(0, 24):
            current_time = datetime.time(hour, 0)
            if current_time not in reserved_times:
                available_times.append((current_time.strftime(
                    "%H:%M"), current_time.strftime("%H:%M")))

        self.fields['time'].choices = available_times


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name']
