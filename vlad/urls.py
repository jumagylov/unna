from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('send', views.SendDataViewSet)
router.register('room', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
