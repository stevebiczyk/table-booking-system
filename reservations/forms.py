from django import forms
from .models import Customer, Reservation, Table
from .models import Staff
from datetime import date, time


class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget, initial=date.today())
    time = forms.TimeInput(format='%H:%M')
    table = forms.ModelChoiceField(queryset=Table.objects.all())

    class Meta:
        model = Reservation
        fields = ['date', 'time', 'number_of_guests', 'special_requests']

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs and 'table' in kwargs['initial'] and 'date' in kwargs['initial']:
            self.update_time_choices(
                kwargs['initial']['table'], kwargs['initial']['date'])

    def update_time_choices(self, table, date):
        reserved_times = Reservation.objects.filter(
            table=table, date=date).values_list('time', flat=True)
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
