from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CategoriaForm
<<<<<<< HEAD
from .models import Categoria

#página inicial do sistema
def home(request):
    categorias = Categoria.objects.all() # Busca tudo no banco de dados
    return render(request, 'cantina/home.html', {'categorias': categorias})

#página de cadastrar categoria
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('home') # <--- MUDAMOS AQUI! Agora volta pra página inicial
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')
    else:
        form = CategoriaForm()

    return render(request, 'cantina/categoria_form.html', {'form': form})
=======

def cadastrar_categoria(request):
    form = CategoriaForm()  

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!') 
            return redirect('/admin/')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')

    return render(request,'cantina/categoria_form.html',{'form': form})
>>>>>>> c2284f8626fa6a0fa2edcdc03a76fdd9f0f69bf4
