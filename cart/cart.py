from django.conf import settings

from product.models import Produto

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            
        self.cart = cart
        
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['produto'] = Produto.objects.get(pk=p)
            
        for item in self.cart.values():
            item['total_price'] = item['produto'].price * item['quantidade']
            
            yield item
            
    def __len__(self):
        return sum(item['quantidade'] for item in self.cart.values()) 
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        
    def add(self, produto_id, quantidade=1, update_quantidade=False):
        produto_id = str(produto_id)
        
        if produto_id not in self.cart:
            self.cart[produto_id] = {'quantidade': 1, 'id': produto_id}
            
        if update_quantidade:
            self.cart[produto_id]['quantidade'] += int(quantidade)
            
            if self.cart[produto_id]['quantidade'] == 0:
                self.remove(produto_id)
                
        self.save()
        
    def remove(self, produto_id):
        if produto_id in self.cart:
            del self.cart[produto_id]
            self.save()
            
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['produto'] = Produto.objects.get(pk=p)
            
        total_cost = sum(item['produto'].price * item['quantidade'] for item in self.cart.values())
        return f'R${total_cost},00'
    
    def get_item(self, produto_id):
        if str(produto_id) in self.cart:
            return self.cart[str(produto_id)]
        else:
            return None