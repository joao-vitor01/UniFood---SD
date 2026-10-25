from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CategoriaForm, ProdutoForm
from .models import Categoria, Produto
from clientes.models import Pedido


# Página inicial do sistema (Kanban)
@login_required
def home(request):
    pedidos = (
        Pedido.objects.select_related('cliente', 'pagamento')
        .prefetch_related('itens__produto')
        .all()
    )

    context = {
        'col_recebido': pedidos.filter(status='recebido'),
        'col_preparo': pedidos.filter(status='preparo'),
        'col_pronto': pedidos.filter(status='pronto'),
        'col_entregue': pedidos.filter(status='entregue').order_by('-criado_em')[:5],
    }
    return render(request, 'cantina/home.html', context)


# Lista os Produtos e Categorias
@login_required
def listar_produtos(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.select_related('categoria').all()

    return render(
        request,
        'cantina/produtos.html',
        {
            'categorias': categorias,
            'produtos': produtos,
        },
    )


# Página de cadastrar categoria
@login_required
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


@login_required
def avancar_status_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    fluxo_status = {
        'recebido': 'preparo',
        'preparo': 'pronto',
        'pronto': 'entregue',
    }

    proximo_status = fluxo_status.get(pedido.status)
    if proximo_status:
        pedido.status = proximo_status
        pedido.save()

    return redirect('home')