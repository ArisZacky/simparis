from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from django.views.generic import (ListView, UpdateView, CreateView, DeleteView)

from .models import RuanganFasilitas
from .forms import RuanganFasilitasForm

from django.contrib import messages
# Create your views here.
     
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RuanganFasilitasListView(ListView):
    model = RuanganFasilitas
    template_name = "ruanganfasilitas/dashboard/listRuanganFasilitas.html"
    context_object_name = 'ruanganFasilitasList'

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


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UpdateRuanganFasilitas(UpdateView):
    form_class = RuanganFasilitasForm
    model = RuanganFasilitas
    template_name = "ruanganfasilitas/dashboard/listRuanganFasilitasUpdate.html"
    success_url = "/ruanganfasilitas/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ruangan Fasilitas berhasil diedit!')
        return response
    
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


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateRuanganFasilitas(CreateView):
    form_class = RuanganFasilitasForm
    model = RuanganFasilitas
    template_name = "ruanganfasilitas/dashboard/listRuanganFasilitasCreate.html"
    success_url = "/ruanganfasilitas/"

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form)
        messages.success(self.request, 'Ruangan Fasilitas berhasil dibuat!')
        return response
    
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

    
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeleteRuanganFasilitas(DeleteView):
    model = RuanganFasilitas
    template_name = "ruanganfasilitas/dashboard/listRuanganFasilitasDelete.html"
    success_url = "/ruanganfasilitas/"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Ruangan Fasilitas berhasil dihapus!')
        return response
    
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
