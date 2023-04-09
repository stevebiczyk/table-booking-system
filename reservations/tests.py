from django.test import TestCase
from django.urls import reverse
from .models import Reservation, Table
from .forms import ReservationForm, CustomerForm


class ReservationModelTests(TestCase):
    def test_reservation_creation(self):
        table = Table.objects.create(name="Test Table", capacity=4)
        reservation = Reservation.objects.create(
            table=table,
            date="2023-05-01",
            time="12:00",
            number_of_guests=2,
            special_requests="Test request"
        )
        self.assertEqual(reservation.table, table)
        self.assertEqual(reservation.date, "2023-05-01")
        self.assertEqual(reservation.time, "12:00")
        self.assertEqual(reservation.number_of_guests, 2)
        self.assertEqual(reservation.special_requests, "Test request")


class CreateBookingViewTests(TestCase):
    def test_create_booking_view_uses_correct_template(self):
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_create_booking_view_form_submission(self):
        table = Table.objects.create(name="Test Table", capacity=4)
        response = self.client.post(reverse('create_booking'), {
            'table': table.id,
            'date': '2023-05-01',
            'time': '12:00',
            'number_of_guests': 2,
            'special_requests': 'Test request',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
        })

        # Redirected to the confirmation page
        self.assertEqual(response.status_code, 302)
        # A reservation has been created
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(Table.objects.count(), 1)  # A table has been created
