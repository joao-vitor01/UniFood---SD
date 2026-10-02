import os
import django
import random
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unifood.settings')
django.setup()

from faker import Faker
from cantina.models import Categoria, Produto, EstoqueDiario
from clientes.models import Cliente, Pedido, ItemPedido, Pagamento

def popular_banco(num_clientes=100, num_pedidos=200):
    fake = Faker('pt_BR')
    
    print("Limpando dados antigos.")
    Categoria.objects.all().delete()
    Cliente.objects.all().delete()

    print("Criando Categorias e Produtos.")
    categorias_nomes = ['Salgados', 'Bebidas', 'Doces', 'Refeições']
    categorias = []
    for nome in categorias_nomes:
        cat = Categoria.objects.create(nome=nome)
        categorias.append(cat)
        
        for _ in range(random.randint(3, 6)):
            prod = Produto.objects.create(
                categoria=cat,
                nome=fake.word().capitalize() + " " + fake.word(),
                preco=Decimal(round(random.uniform(2.50, 25.00), 2))
            )
            EstoqueDiario.objects.create(
                produto=prod,
                quantidade=random.randint(10, 50)
            )

    produtos = list(Produto.objects.all())

    print(f"Criando {num_clientes} Clientes (Estudantes).")
    clientes = []
    for _ in range(num_clientes):
        cli = Cliente.objects.create(
            nome=fake.name(),
            matricula=fake.unique.numerify(text='202######'),
            email=fake.unique.email()
        )
        clientes.append(cli)

    print(f"Criando {num_pedidos} Pedidos, Itens e Pagamentos.")
    status_pedido = ['Recebido', 'Preparando', 'Pronto', 'Entregue', 'Cancelado']
    status_pagamento = ['Pendente', 'Aprovado', 'Recusado']
    metodos_pagamento = ['PIX', 'Cartão de Crédito', 'Cartão de Débito', 'Dinheiro']

    for _ in range(num_pedidos):
        pedido = Pedido.objects.create(
            cliente=random.choice(clientes),
            status=random.choice(status_pedido),
            codigo_retirada=fake.lexify(text='???-####').upper()
        )
        
        produtos_escolhidos = random.sample(produtos, random.randint(1, 4))
        for prod in produtos_escolhidos:
            ItemPedido.objects.create(
                pedido=pedido,
                produto=prod,
                quantidade=random.randint(1, 3)
            )
            
        Pagamento.objects.create(
            pedido=pedido,
            status=random.choice(status_pagamento),
            metodo=random.choice(metodos_pagamento)
        )

    print("Banco de dados populado com sucesso!")

if __name__ == '__main__':
    popular_banco()