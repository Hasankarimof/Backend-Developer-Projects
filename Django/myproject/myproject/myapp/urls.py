from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking_view, name='booking'),
    path('success/', views.success_view, name='success_page'),
    path('success/', views.success_view, name='success_page'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('register/', views.register_view, name='register'),
    path('index/', views.index),
    path('about/', views.about),
    path('menu/', views.menu),
    path('menu_card/', views.menu_by_id),
    path('homee/', views.homee),
    path('aboutt/', views.aboutt),
    path('menuu/', views.menuu),
]
