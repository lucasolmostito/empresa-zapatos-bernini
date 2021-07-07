from django import forms
from django.forms import fields, widgets

from .models import Item, ItemInShoppingCart

class SearchItemForm(forms.ModelForm):
    """ Form to add products and quantity to the order """
    
    class Meta:
        model = ItemInShoppingCart
        fields = ('item', 'quantity')
        widgets = {
            'item': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        
    def clean_quantity(self):
        """ We validate that the quantities do not excedd the stock and are less than zero """
        
        quantity = self.cleaned_data['quantity']
        item = self.cleaned_data['item']
        
        # We check if this product currently in the Shopping Cart
        item_in_cart = ItemInShoppingCart.objects.filter(item=item).exists()
        # We recover the stock of the item
        stock = Item.objects.get(id=item.id).stock
        
        if item_in_cart:
            current_quantity = ItemInShoppingCart.objects.get(item=item).quantity
            total_quantity = quantity + current_quantity
        else:
            total_quantity = quantity
 
        if total_quantity > stock:
            raise forms.ValidationError('Cantidad excedida, el stock total de este producto es de ' + str(stock))
        elif quantity < 1:
            raise forms.ValidationError('No puedes ingresar una cantidad de 0')
        
        return quantity
        