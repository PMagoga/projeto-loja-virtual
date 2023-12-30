from django.shortcuts import render, get_object_or_404

from .models import Produto

def produto(request, slug):
    
    produto = get_object_or_404(Produto, slug=slug)
    
    return render(request, 'product/produto.html', {'produto': produto})
