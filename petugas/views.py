from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import CustomUserChangeForm, CustomUserCreationForm

from login.models import Petugas

from django.views.generic import (CreateView, UpdateView, DeleteView, ListView)

# Create your views here.
# def = function

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PetugasListView(ListView):
    model = Petugas
    template_name = "petugas/dashboard/listPetugas.html"
    context_object_name = 'petugasList'

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
class UpdatePetugas(UpdateView):
    form_class = CustomUserCreationForm
    model = Petugas
    template_name = "petugas/dashboard/listPetugasUpdate.html"
    success_url = "/petugas/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Petugas berhasil diedit!')
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
class CreatePetugas(CreateView):
    model = Petugas
    form_class = CustomUserCreationForm
    template_name = 'petugas/dashboard/listPetugasCreate.html'
    success_url = "/petugas/"

    def form_valid(self, form):
        form.save()
        
        self.send_welcome_email(form.cleaned_data['namaPetugas'], form.cleaned_data['email'], form.cleaned_data['password1'], form.cleaned_data['level'])

        response = super().form_valid(form)
        messages.success(self.request, 'Petugas berhasil dibuat!')
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
    
    def send_welcome_email(self, namaPetugas, email, password1, level):
        subject = 'Akun Anda Telah Didaftarkan!'
        message = f'Hai {namaPetugas}, you are registered by admin as {level}, with email: {email}, and password: {password1}. We appreciate your works.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeletePetugas(DeleteView):
    model = Petugas
    template_name = "petugas/dashboard/listPetugasDelete.html"
    success_url = "/petugas/"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Petugas berhasil dihapus!')
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