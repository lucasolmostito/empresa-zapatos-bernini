import csv

from io import StringIO
from django.utils import timezone
from django.core.mail import EmailMessage

from applications.items.models import ItemInShoppingCart, Item
from .models import Order, OrderDetail

def order_process(self, **kwargs):
    """ This function performs total order processing and order details """
    
    items_in_cart = ItemInShoppingCart.objects.filter(
        user=kwargs['user']
    )
    
    if items_in_cart.count() > 0:
        
        all_order = Order.objects.create(
            user=kwargs['user'],
            date_sale=timezone.now(),
            total_quantity=0,
            total_amount=0
        )
        
        list_order_detail = []
        list_items = []
        
        for item in items_in_cart:
                        
            order_detail = OrderDetail(
                order=all_order,
                item=Item.objects.get(name=item.item.name),
                quantity=item.quantity,
                price=item.item.sale_price
            )
            
            # we modify the total quantity and amount of the entire sale
            all_order.total_quantity += item.quantity
            all_order.total_amount += item.item.sale_price * item.quantity
            
            # we update the stock
            items = item.item
            items.stock -= item.quantity
            
            list_order_detail.append(order_detail)
            list_items.append(items)
        
        all_order.save()
        
        # We create and update the records.
        OrderDetail.objects.bulk_create(list_order_detail)
        Item.objects.bulk_update(list_items, ['stock'])
        
        items_in_cart.delete()
        
        # We send the email
        send_order(all_order)
           
        return all_order
        
    return None

def send_order(all_order):
    """ This function sends the email with the order in csv format """
    
    # We retrieve a list of the corresponding order details
    list_order_details = OrderDetail.objects.filter(
            order = all_order
        )
    
    # We create the order in csv format
    csvfile = StringIO()
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Cliente', 'ID Venta', 'Producto', 'Cantidad', 'Precio'])
    for order in list_order_details:
        csvwriter.writerow([order.order.user.full_name, order.order.id, order.item.name, order.quantity, order.price])

    message = EmailMessage(
        'Información de pedido',
        order.order.user.full_name + ' con correo electrónico ' + order.order.user.email + ' ha realizado un pedido',
        'lucasfernandoolmos@gmail.com',
        ['lucasfernandoolmos@gmail.com'],
    )
    message.attach('order-'+ str(order.order.id) +'.csv', csvfile.getvalue(), 'text/csv')
    message.send()
    
    return None