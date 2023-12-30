from django.shortcuts import render, redirect

from cart.cart import Cart
from .models import Order, OrderItem


def start_order(request):
    
    cart = Cart(request)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        
        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email,
                                     address=address, zipcode=zipcode, place=place, phone=phone)
        
        for item in cart:
            produto = item['produto']
            quantidade = int(item['quantidade'])
            price = produto.price * quantidade
            
            item = OrderItem.objects.create(order=order, produto=produto, price=price,
                                            quantidade=quantidade)
            
        return redirect('myaccount')
    return redirect('cart')