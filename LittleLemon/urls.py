from django.contrib import admin
from django.urls import path, include
from reservation import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', include('reservation.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/',include('reservation.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]