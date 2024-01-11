from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from django.views.generic import (ListView, UpdateView, CreateView, DeleteView)

from .models import Fasilitas
from .forms import FasilitasForm

from django.contrib import messages
# Create your views here.
     
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FasilitasListView(ListView):
    model = Fasilitas
    template_name = "fasilitas/dashboard/listFasilitas.html"
    context_object_name = 'fasilitasList'

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
class UpdateFasilitas(UpdateView):
    form_class = FasilitasForm
    model = Fasilitas
    template_name = "fasilitas/dashboard/listFasilitasUpdate.html"
    success_url = "/fasilitas/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Fasilitas berhasil diedit!')
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
class CreateFasilitas(CreateView):
    form_class = FasilitasForm
    model = Fasilitas
    template_name = "fasilitas/dashboard/listFasilitasCreate.html"
    success_url = "/fasilitas/"

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form)
        messages.success(self.request, 'Fasilitas berhasil dibuat!')
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
class DeleteFasilitas(DeleteView):
    model = Fasilitas
    template_name = "fasilitas/dashboard/listFasilitasDelete.html"
    success_url = "/fasilitas/"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Fasilitas berhasil dihapus!')
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
