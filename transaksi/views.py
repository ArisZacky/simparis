from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.conf import settings
from midtransclient import CoreApi
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.views.generic import (ListView, View)
from .models import Transaksi
# Create your views here.
     
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TransaksiListView(ListView):
    model = Transaksi
    template_name = "transaksi/dashboard/listTransaksi.html"
    context_object_name = 'transaksiList'

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
    

midtrans = CoreApi(
    is_production=settings.MIDTRANS['is_production'],
    server_key=settings.MIDTRANS['server_key'],
    client_key=settings.MIDTRANS['client_key']
)

class CreateOrderView(View):
    template_name = 'create_order.html'

    def get(self, request, *args, **kwargs):
        # Logika untuk membuat order di database

        # Contoh order_id, total_amount, dan item_details
        order_id = 'ORDER123'
        total_amount = 100000  # Rupiah
        item_details = [{'id': 'item1', 'price': 100000, 'quantity': 1, 'name': 'Item 1'}]

        # Membuat payload untuk Midtrans
        transaction_details = {
            'order_id': order_id,
            'gross_amount': total_amount,
        }
        credit_card_option = {
            'secure': True,
        }
        payment_params = {
            'transaction_details': transaction_details,
            'credit_card': credit_card_option,
            'item_details': item_details,
        }

        # Mendapatkan token pembayaran dari Midtrans
        try:
            token = midtrans.snap.create_transaction(payment_params).json()['token']
        except Exception as e:
            return JsonResponse({'error': str(e)})

        return render(request, self.template_name, {'token': token})

@method_decorator(csrf_exempt, name='dispatch')
class PaymentNotificationView(View):
    def post(self, request, *args, **kwargs):
        # Logika untuk menangani notifikasi pembayaran dari Midtrans
        # ...

        return JsonResponse({'status': 'ok'})