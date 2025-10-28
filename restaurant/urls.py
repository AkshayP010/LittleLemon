from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]