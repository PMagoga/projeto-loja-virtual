from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from product.models import Produto, Categoria

from .forms import SignUpForm

def frontpage(request):
    produtos = Produto.objects.all()[0:8]
    
    return render(request, 'core/frontpage.html', {'produtos': produtos})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('/')
    else:
        form = SignUpForm()
        
    return render(request, 'core/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':        
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        
        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')


def loja(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    
    active_categoria = request.GET.get('categoria', '')
    
    if active_categoria:
        produtos = produtos.filter(categoria__slug=active_categoria)
        
    query = request.GET.get('query', '')
    
    if query:
        produtos = produtos.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'categorias': categorias,
        'produtos': produtos,
        'active_categoria': active_categoria
    }
    
    return render(request, 'core/loja.html', context)


def credito(request):
    return render(request, 'core/credito.html')