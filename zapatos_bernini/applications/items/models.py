from timestampedmodel import TimestampedModel

from django.db import models
from django.conf import settings 

from .managers import ItemInShoppingCartManager


class Category(TimestampedModel):
    
    name = models.CharField('Categoria', max_length=20)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.name
    

class Item(TimestampedModel):
    """ Model to represent the items in the store """
    
    name = models.CharField('Nombre', max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sale_price = models.DecimalField('Precio de venta', max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField('Cantidad disponible', default=0)
    available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        
    def __str__(self):
        return self.name


class ItemInShoppingCart(TimestampedModel):
    """ Model to represent the items in the Shoping Cart """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Cantidad', default=1)
    
    objects = ItemInShoppingCartManager()
    
    class Meta:
        verbose_name = 'Artículo en carrito'
        verbose_name_plural = 'Artículos en carrito'
        
    def __str__(self):
        return self.item.name