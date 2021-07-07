from django.urls import path

from . import views

app_name = 'app_orders'

urlpatterns = [
    path('enviar-pedido/', views.SendOrderView.as_view(), name='send-order'),
]
