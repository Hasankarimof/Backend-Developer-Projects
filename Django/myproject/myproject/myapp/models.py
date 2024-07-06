from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    guest_count = models.IntegerField()
    reservation_time = models.DateTimeField()
    comments = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

class Reservation(models.Model):
    name = models.CharField(max_length=100,blank=True)
    contact = models.CharField('Phone number',max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self) -> str:
        return self.name


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this line
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this line
        blank=True,
        help_text='Specific permissions for this usser.',
        related_query_name='customuser',
    )


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

