from django.shortcuts import render
from django.views.generic import FormView, View
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .forms import SearchItemForm
from .models import Item, ItemInShoppingCart
from applications.users.mixins import TestPermissionMixin

from .serializers import ItemDetailSerializer, ItemSerializer, ItemPagination


class AddItemFormView(TestPermissionMixin, FormView):
    """ We add the items to the order """
    
    template_name = 'items/shopping_cart.html'
    form_class = SearchItemForm
    success_url = '.'
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['list_items'] = ItemInShoppingCart.objects.get_items_list(user)
        return context
    
    def form_valid(self, form):
        item = form.cleaned_data['item']
        quantity = form.cleaned_data['quantity']
        
        # If it already exists in the cart, only the quantity is added.
        obj, created = ItemInShoppingCart.objects.get_or_create(
            item=item,
            defaults={
                'user' : self.request.user,
                'quantity' : quantity 
            }
        )
        
        if not created:
            obj.quantity += quantity
            obj.save()
        
        return super(AddItemFormView, self).form_valid(form)


class SubtractQuantityItemView(TestPermissionMixin, View):
    """ We subtract the quantity of the item in the shopping cart """
    
    def post(self, request, *args, **kwargs):
        item = ItemInShoppingCart.objects.get(
            user=self.request.user,
            id=self.kwargs['pk']
        )
        
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
            
        return HttpResponseRedirect(
            reverse('app_items:add-item')
        ) 
        
class AddQuantityItemView(TestPermissionMixin, View):
    """ We add the quantity of the item in the shopping cart """

    
    def post(self, request, *args, **kwargs):
        item = ItemInShoppingCart.objects.get(
            user=self.request.user,
            id=self.kwargs['pk']
        )
        
        if item.quantity < item.item.stock:
            item.quantity += 1
            item.save()
            
        return HttpResponseRedirect(
            reverse('app_items:add-item')
        )       
    

class ItemCartDeleteView(TestPermissionMixin, DeleteView):
    """ We remove the item from the shopping cart """
    
    model = ItemInShoppingCart
    success_url = reverse_lazy('app_items:add-item')
    

class ItemsListApiView(ListAPIView):
    """ 
    Retorna todos los artículos disponibles
    """
    serializer_class = ItemSerializer
    pagination_class = ItemPagination
    
    def get_queryset(self):
        return Item.objects.all()
    

class ItemDetailApiView(RetrieveAPIView):
    """
    Retorna los detalles de un artículo
    """
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()
    