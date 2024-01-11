from django.urls import path

from . import views

urlpatterns = [
    path('room-details/<slug:slug>/', views.RoomDetail.as_view(), name="Room-Details"),
    path('ruanganList/', views.RuanganListView.as_view(), name="ruanganList"),
    path('ruanganList/update/<int:pk>', views.UpdateRuangan.as_view(), name="ruanganListUpdate"),
    path('ruanganList/delete/<int:pk>', views.DeleteRuangan.as_view(), name="ruanganListDelete"),
    path('ruanganList/create/', views.CreateRuangan.as_view(), name="ruanganListCreate")
]