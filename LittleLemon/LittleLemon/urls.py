
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.views import MenuItemViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/registration/', include('rest_auth.registration.urls')),
]
            