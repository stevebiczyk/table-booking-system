from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from reservations.models import *


class TestViews(TestCase):

    # def setUp(self):
    #     self.client = Client()
    #     self.user = User.objects.create_user(
    #         username='testuser', password='12345')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_menu_view(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    # def test_create_booking_view(self):
    #     self.client.login(username='testuser', password='12345')
    #     response = self.client.get(reverse('create_booking'))
    #     self.assertEqual(response.status_code, 200)

    # def test_bookings_list_view(self):
    #     self.client.login(username='testuser', password='12345')
    #     response = self.client.get(reverse('bookings_list'))
    #     self.assertEqual(response.status_code, 200)
