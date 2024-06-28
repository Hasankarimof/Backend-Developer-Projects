
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_time = models.DateTimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"{self.name} booking for {self.number_of_people} at {self.booking_time}"
            