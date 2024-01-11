from django.urls import path

from . import views

urlpatterns = [
    path('listTransaksi/', views.TransaksiListView.as_view(), name="transaksiList"),
]