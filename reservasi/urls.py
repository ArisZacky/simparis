from django.urls import path

from . import views

urlpatterns = [
    path('listReservasi/', views.ReservasiListView.as_view(), name="reservasiList"),
]