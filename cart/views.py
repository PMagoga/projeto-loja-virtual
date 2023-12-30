from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .cart import Cart

from product.models import Produto

def add_to_cart(request, produto_id):
    cart = Cart(request)
    cart.add(produto_id)
    
    return render(request, 'cart/menu_cart.html')

def cart(request):
    return render(request, 'cart/cart.html')

def update_cart(request, produto_id, action):
    cart = Cart(request)
    
    if action == 'increment':
        cart.add(produto_id, 1, True)
    else:
        cart.add(produto_id, -1, True)

    produto = Produto.objects.get(pk=produto_id)
    quantidade = cart.get_item(produto_id)
    
    if quantidade:
        quantidade = quantidade['quantidade']
    
        item = {
            'produto' : {
                'id': produto_id,
                'name': produto.name,
                'image': produto.image,
                'get_thumbnail': produto.get_thumbnail,
                'price': produto.price,
            },
            'total_price': (quantidade * produto.price),
            'quantidade': quantidade
        }
    else:
        item = None
    
    response = render(request, 'cart/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'
    
    return response


@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')

def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')