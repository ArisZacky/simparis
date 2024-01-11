from django.urls import path

from . import views

urlpatterns = [
    path('', views.FasilitasListView.as_view(), name="fasilitasList"),
    path('update/<int:pk>', views.UpdateFasilitas.as_view(), name="fasilitasListUpdate"),
    path('delete/<int:pk>', views.DeleteFasilitas.as_view(), name="fasilitasListDelete"),
    path('create/', views.CreateFasilitas.as_view(), name="fasilitasListCreate")
]