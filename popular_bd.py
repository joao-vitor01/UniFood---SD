import os
import django
import random
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unifood.settings')
django.setup()

from faker import Faker
from cantina.models import Categoria, Produto, EstoqueDiario
from clientes.models import Cliente, Pedido, ItemPedido, Pagamento

# Catálogo realista dividido por categoria
CARDAPIO_REAL = {
    'Salgados': [
        ('Coxinha de Frango com Catupiry', 7.50),
        ('Empada de Frango', 6.50),
        ('Pão de Queijo Tradicional', 5.00),
        ('Enroladinho de Presunto e Queijo', 6.50),
        ('Pastel de Forno de Carne', 7.00),
        ('Esfiha de Carne', 6.50),
    ],
    'Bebidas': [
        ('Café Coado 150ml', 3.00),
        ('Refrigerante Lata 350ml', 6.00),
        ('Suco de Laranja Natural 400ml', 7.50),
        ('Água Mineral sem Gás 500ml', 3.50),
        ('Cappuccino Cremoso', 6.50),
        ('Suco de Maracujá 400ml', 7.00),
    ],
    'Doces': [
        ('Brigadeiro Tradicional', 3.50),
        ('Brownie de Chocolate', 8.00),
        ('Fatia de Bolo de Cenoura', 6.00),
        ('Cookie com Gotas de Chocolate', 5.50),
    ],
    'Refeições': [
        ('Misto Quente na Chapa', 9.00),
        ('Sanduíche Natural de Frango', 11.50),
        ('Tapioca de Frango com Queijo', 12.00),
        ('Cuscuz com Ovo e Manteiga', 8.50),
    ]
}

def popular_banco(num_clientes=100, num_pedidos=200):
    fake = Faker('pt_BR')
    
    print("Limpando dados antigos.")
    Pagamento.objects.all().delete()
    ItemPedido.objects.all().delete()
    Pedido.objects.all().delete()
    EstoqueDiario.objects.all().delete()
    Produto.objects.all().delete()
    Categoria.objects.all().delete()
    Cliente.objects.all().delete()

    print("Criando Categorias e Produtos.")
    todos_produtos=[]
    for nome_cat, itens in CARDAPIO_REAL.items():
        cat = Categoria.objects.create(nome=nome_cat)

        for nome_prod, preco_prod in itens:
            prod = Produto.objects.create(
                categoria=cat,
                nome=nome_prod,
                preco=Decimal(str(preco_prod))
            )
            todos_produtos.append(prod)

            EstoqueDiario.objects.create(
                produto=prod,
                quantidade=random.randint(15, 60)
            )

    print(f"Criando {num_clientes} Clientes.")
    clientes=[]
    for _ in range(num_clientes):
        cli = Cliente.objects.create(
            nome=fake.name(),
            cpf=fake.cpf(),
            email=fake.unique.email()
        )
        clientes.append(cli)

    print(f"Criando {num_pedidos} Pedidos alinhados com o Kanban.")

    status_pedido = ['recebido', 'preparando', 'pronto', 'entregue']
    status_pagamento = ['pendente', 'aprovado', 'recusado']
    metodos_pagamento = ['PIX', 'Cartão de Crédito', 'Cartão de Débito', 'Dinheiro']

    contador_codigo = 100
    letras = ['A', 'B', 'C']

    for _ in range(num_pedidos):
        contador_codigo +=1
        codigo = f"{random.choice(letras)}{contador_codigo}"

        pedido = Pedido.objects.create(
            cliente=random.choice(clientes),
            status=random.choice(status_pedido),
            codigo_retirada=codigo
        )
        
        produtos_escolhidos = random.sample(todos_produtos, random.randint(1, 3))
        for prod in produtos_escolhidos:
            ItemPedido.objects.create(
                pedido=pedido,
                produto=prod,
                quantidade=random.randint(1, 2)
            )
            
        Pagamento.objects.create(
            pedido=pedido,
            status=random.choice(status_pagamento),
            metodo=random.choice(metodos_pagamento)
        )

    print("Banco de dados populado com sucesso!")

if __name__ == '__main__':
    popular_banco()