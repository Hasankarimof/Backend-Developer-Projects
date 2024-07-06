from django.contrib import admin
from .models import Booking,Contact,Reservation,Menu
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(Menu)
