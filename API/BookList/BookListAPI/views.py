from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import MenuItem
from rest_framework import response

# Create your views here.


@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    return response(items.values())


