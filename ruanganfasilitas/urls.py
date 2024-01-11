from django.urls import path

from . import views

urlpatterns = [
    path('', views.RuanganFasilitasListView.as_view(), name="ruanganFasilitasList"),
    path('update/<int:pk>', views.UpdateRuanganFasilitas.as_view(), name="ruanganFasilitasListUpdate"),
    path('delete/<int:pk>', views.DeleteRuanganFasilitas.as_view(), name="ruanganFasilitasListDelete"),
    path('create/', views.CreateRuanganFasilitas.as_view(), name="ruanganFasilitasListCreate")
]