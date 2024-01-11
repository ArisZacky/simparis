from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from django.views.generic import (ListView)
from ruangan.models import Reservasi
# Create your views here.
     
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ReservasiListView(ListView):
    model = Reservasi
    template_name = "reservasi/dashboard/listReservasi.html"
    context_object_name = 'reservasiList'

    def test_func(self):
        user_level = self.request.user.level
        return user_level == 'admin' or user_level == 'petugas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_level = self.request.user.level
        context['namaPetugas'] = self.request.user.namaPetugas
        
        if user_level == 'admin':
            context['title'] = 'Dashboard Admin Simparis'
            context['level'] = 'admin'
        elif user_level == 'petugas':
            context['title'] = 'Dashboard Petugas Simparis'
            context['level'] = 'petugas'
        return context