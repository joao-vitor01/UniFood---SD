from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CategoriaForm

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
