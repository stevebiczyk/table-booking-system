from django import forms
from .models import Customer, Reservation
from .models import Staff


class ReservationForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(), widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time',
                  'number_of_guests', 'special_requests']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name']
