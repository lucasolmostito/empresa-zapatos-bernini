from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import ModelState
from django.conf import settings

from timestampedmodel import TimestampedModel

from applications.items.models import Item


class Order(TimestampedModel):
    """ Model representing all the details of a complete order """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_sale = models.DateTimeField()
    total_quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField('Monto total', max_digits=7, decimal_places=2)
    canceled = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        
    def __str__(self):
        return str(self.id) + ' - ' + str(self.date_sale)
    

class OrderDetail(TimestampedModel):
    """ Model that represents the details of the sale of a product """
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Cantidad de un producto')
    price = models.DecimalField('Precio', max_digits=7, decimal_places=2)
    canceled = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Detalle de pedido'
        verbose_name_plural = 'Detalles de pedido'
        
    def __str__(self):
        return 'Pedido' + '[' + str(self.order.id) + ']'
