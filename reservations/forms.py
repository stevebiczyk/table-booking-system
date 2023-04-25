from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation, Table
from .models import Staff
import datetime
from datetime import date, time


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget, initial=date.today())
    time = forms.TimeField(
        input_formats=['%H:%M'],
        # Input field with 24-hour format and 30-minute intervals
        widget=forms.TimeInput(
            attrs={'type': 'time', 'step': '1800'}, format='%H:%M')
    )
    table = forms.ModelChoiceField(queryset=Table.objects.all(), required=True)
    # Limiting number of guests to 25 people
    number_of_guests = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(25)]
    )

    class Meta:
        model = Reservation
        fields = ['date', 'time', 'number_of_guests', 'special_requests']

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs and 'table' in kwargs['initial'] and 'date' in kwargs['initial']:
            self.update_time_choices(
                kwargs['initial']['table'], kwargs['initial']['date'])

    def clean(self):
        cleaned_data = super().clean()
        reservation_time = cleaned_data.get("time")
        opening_time = datetime.time(hour=9, minute=0)
        closing_time = datetime.time(hour=21, minute=0)
        # opening_time = datetime.time(9, 0)
        # closing_time = datetime.time(21, 0)

        # Check if the reservation time is within opening hours
        if reservation_time is not None and (reservation_time < opening_time or reservation_time >= closing_time):
            raise ValidationError(
                "Please choose a reservation time between 09:00 and 21:00."
            )

            # Check if the selected date and time are in the past
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        if date and time:
            now = datetime.datetime.now()
            reservation_datetime = datetime.datetime.combine(date, time)
            if reservation_datetime < now:
                raise ValidationError(
                    "You cannot make a booking for a past date and time.")
        return cleaned_data


def update_time_choices(self, table, date):
    reserved_times = Reservation.objects.filter(
        table=table, date=date).values_list('time', flat=True)
    available_times = []

    for hour in range(9, 21):
        current_time = datetime.time(hour, 0)
        if current_time not in reserved_times:
            available_times.append((current_time.strftime(
                "%H:%M"), current_time.strftime("%H:%M")))

    self.fields['time'].choices = available_times


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name']


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email', 'phone')
