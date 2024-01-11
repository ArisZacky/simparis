from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.conf import settings

from django.views.generic import (ListView, DetailView, UpdateView, CreateView, DeleteView)
from django.utils import timezone
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from django.http import JsonResponse

from .models import Ruangan, Reservasi
from fasilitas.models import Fasilitas
from .forms import CheckAvail, Reservation, RuanganForm

from django.contrib import messages
# Create your views here.

class RoomDetail(DetailView):
    model = Ruangan
    # slug_field = "namaRuangan"
    template_name = "ruangan/room_detail.html"
    context_object_name = 'ruangan'
    # slug_url_kwarg = 'idRuangan'
    context = {
        'title':'Room Details',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ruanganId = self.object.idRuangan
        context['ruanganId'] = ruanganId
       
        # Queryset untuk mendapatkan data yang diinginkan
        fasilitas = Fasilitas.objects.filter(
            ruanganfasilitas__idRuangan=ruanganId
        ).values(
            'namaFasilitas',
            'ruanganfasilitas__jumlahBarang',
            'ruanganfasilitas__idRuangan'
        )
        context['listFasilitas'] = fasilitas
        return context
    
    def post(self, request, *args, **kwargs):
        if 'check_availability' in request.POST:
            #HANDLE CHECK AVAILABILITY
            form = CheckAvail(request.POST)
            if form.is_valid():
                ruangan = request.POST['idRuangan']
                checkInDate = form.cleaned_data['checkIn']
                checkOutDate = form.cleaned_data['checkOut']

                available_rooms = Reservasi.objects.filter(
                    idRuangan = ruangan,
                    checkIn = checkInDate,
                    checkOut = checkOutDate
                )

                cekRuangan = Ruangan.objects.filter(
                    idRuangan = ruangan
                ).first()

                hargaRuangan = cekRuangan.harga

                #Cek jika checkIn setelah checkOut
                if checkInDate and checkOutDate and checkInDate > checkOutDate:
                    response = JsonResponse({'success': False, 'message': "Sorry, Check In date cannot after Check Out date"})
                    return response
                
                #Cek jika checkIn atau checkOut ada di masa lalu
                today = timezone.now().date()
                if checkInDate and checkInDate < today:
                    response = JsonResponse({'success': False, 'message': "Sorry, Check In date cannot be in the past."})
                    return response

                if checkOutDate and checkOutDate < today:
                    response = JsonResponse({'success': False, 'message': "Sorry, Check Out date cannot be in the past."})
                    return response

                if available_rooms.exists():
                    #IF RUANGAN NOT AVAILABLE
                    response = JsonResponse({'success': False, 'message': 'Sorry, Room not available for selected dates.',  'checkIn': checkInDate, 'checkOut': checkOutDate, 'idRuangan': ruangan}) 
                    return response
                else: 
                    #IF RUANGAN AVAILABLE
                    response = JsonResponse({'success': True, 'message': 'Room available for selected dates.', 'checkIn': checkInDate, 'checkOut': checkOutDate, 'idRuangan': ruangan, 'total': hargaRuangan})
                    return response
            else:
                #IF FORM IS NOT VALID
                response = JsonResponse({'success': False, 'message': 'Invalid form data.'})
                return response
        
        elif 'complete_reservation' in request.POST:
            #HANDLE POST REQUEST FOR COMPLETING RESERVATION
            form = Reservation(request.POST)
            if form.is_valid():
                ruangan = request.POST['idRuangan']
                checkInDate = request.POST['checkIn']
                checkOutDate = request.POST['checkOut']
      
                namaRuangan = form.cleaned_data['idRuangan']

                #SEND EMAIL TO REGISTERED EMAIL
                self.send_email(request, namaRuangan)

                form.save()
                response = JsonResponse({'success': True, 'message': 'Reservation Completed, please check your email for the invoice details.'})
                return response
            else:
                response = JsonResponse({'success': False, 'message': 'Invalid form data.'})
                return response
        else:
            response = JsonResponse({'success': False, 'message': 'Invalid request.'})
            return response
    
    def send_email(self, request, namaRuangan):
        namaPelanggan = request.POST['namaPelanggan']
        email = request.POST['email']
        total = request.POST['total']
        checkInDate = request.POST['checkIn']
        checkOutDate = request.POST['checkOut']

        link = "instagram.com"
        #SEND EMAIL TO REGISTERED EMAIL
        subject = 'Reservasi Hotel SIMPARIS'
        email_content = render_to_string("ruangan/template_email.html", {'namaPelanggan': namaPelanggan, 'checkIn': checkInDate, 'checkOut': checkOutDate, 'idRuangan': namaRuangan, 'total': total, 'link': link})
        message = f"Dear {namaPelanggan}, Reservasi anda telah berhasil"
        from_email = settings.EMAIL_HOST_USER
        to_email = email

        msg = EmailMultiAlternatives(subject, message, from_email, [to_email])
        msg.attach_alternative(email_content, "text/html")
        msg.send()

        
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RuanganListView(ListView):
    model = Ruangan
    template_name = "ruangan/dashboard/listRuangan.html"
    context_object_name = 'ruanganList'

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
class UpdateRuangan(UpdateView):
    form_class = RuanganForm
    model = Ruangan
    template_name = "ruangan/dashboard/listRuanganUpdate.html"
    success_url = "/rooms/ruanganList/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ruangan berhasil diedit!')
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
class CreateRuangan(CreateView):
    form_class = RuanganForm
    model = Ruangan
    template_name = "ruangan/dashboard/listRuanganCreate.html"
    success_url = "/rooms/ruanganList/"

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form)
        messages.success(self.request, 'Ruangan berhasil dibuat!')
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
class DeleteRuangan(DeleteView):
    model = Ruangan
    template_name = "ruangan/dashboard/listRuanganDelete.html"
    success_url = "/rooms/ruanganList/"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Ruangan berhasil dihapus!')
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
