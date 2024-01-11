"""
URL configuration for simparis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', include(('login.urls', 'login'), namespace="login")),
    path('logout/', include(('login.urls', 'logoutView'), namespace="logout")),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace="dashboard")),
    path('rooms/', include(('ruangan.urls', 'ruangan'), namespace="ruangan")),
    path('fasilitas/', include(('fasilitas.urls', 'fasilitas'), namespace="fasilitas")),
    path('ruanganfasilitas/', include(('ruanganfasilitas.urls', 'ruanganfasilitas'), namespace="ruanganfasilitas")),
    path('petugas/', include(('petugas.urls', 'petugas'), namespace="petugas")),
    path('reservasi/', include(('reservasi.urls', 'reservasi'), namespace="reservasi")),
    path('transaksi/', include(('transaksi.urls', 'transaksi'), namespace="transaksi")),

]
