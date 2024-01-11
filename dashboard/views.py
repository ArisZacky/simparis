from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import (ListView, UpdateView)
from ruangan.models import Reservasi, Ruangan
from transaksi.models import Transaksi

from django.db.models import Sum
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DashboardView(ListView):
    model = Transaksi
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'transaksi_list'
    login_url = '/login/'

    def get_queryset(self):
        return Transaksi.objects.select_related('idReservasi__idRuangan')
    
    def test_func(self):
        user_level = self.request.user.level
        return user_level == 'admin' or user_level == 'petugas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_level = self.request.user.level
        context['namaPetugas'] = self.request.user.namaPetugas

        jumlahReservasi = Reservasi.objects.count()
        context['jumlahReservasi'] = jumlahReservasi

        totalPendapatan = Reservasi.objects.aggregate(Sum('total'))['total__sum']
        context['totalPendapatan'] = totalPendapatan

        if user_level == 'admin':
            context['title'] = 'Dashboard Admin Simparis'
            context['level'] = 'admin'
        elif user_level == 'petugas':
            context['title'] = 'Dashboard Petugas Simparis'
            context['level'] = 'petugas'
        return context
