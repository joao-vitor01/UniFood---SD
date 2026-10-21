from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CategoriaForm
from .models import Categoria, Produto


#página inicial do sistema
def home(request):
    categorias = Categoria.objects.all() 
    return render(request, 'cantina/home.html', {'categorias': categorias})


#página de cadastrar categoria
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('produtos')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')
    else:
        form = CategoriaForm()

    return render(request, 'cantina/categoria_form.html', {'form': form})

#Lista os Produtos e Categorias
def listar_produtos(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all() 

    return render(request, 'cantina/produtos.html', {'categorias': categorias,'produtos': produtos})