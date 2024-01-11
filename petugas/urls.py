from django.urls import path

from . import views

urlpatterns = [
    path('', views.PetugasListView.as_view(), name="petugasList"),
    path('update/<int:pk>', views.UpdatePetugas.as_view(), name="petugasListUpdate"),
    path('delete/<int:pk>', views.DeletePetugas.as_view(), name="petugasListDelete"),
    path('create/', views.CreatePetugas.as_view(), name="petugasListCreate")

]