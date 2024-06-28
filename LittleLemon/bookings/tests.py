
from django.test import TestCase
from rest_framework.test import APIClient
from .models import MenuItem, Booking

class MenuItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(name="Pasta", description="Delicious", price="10.99")

    def test_get_menu(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)

class BookingTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Booking.objects.create(name="John Doe", booking_time="2023-01-01T12:00:00Z", number_of_people=4)

    def test_get_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)
            