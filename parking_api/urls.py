from django.conf.urls import url
from django.urls import path, include
from .views import (
    ParkingApiView,
    ParkingDetailApiView
)
urlpatterns = [
    path('api', ParkingApiView.as_view()),
    path('api/<int:lot_id>/', ParkingDetailApiView.as_view()),
]