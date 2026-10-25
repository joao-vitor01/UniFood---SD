import re
from django.db import models
from django.core.exceptions import ValidationError
from cantina.models import Produto

def validar_cpf(valor):
    cpf = re.sub(r'[^0-9]', '', str(valor))
    
    if len(cpf) != 11 or len(set(cpf)) == 1:
        raise ValidationError('CPF inválido.')
    
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            raise ValidationError('CPF inválido.')


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True, validators=[validar_cpf])
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('recebido', 'Recebido'),
        ('preparo', 'Em Preparo'),
        ('pronto', 'Pronto'),
        ('entregue', 'Entregue'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='recebido')
    codigo_retirada = models.CharField(max_length=10, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['criado_em']

    def __str__(self):
        return f"Pedido {self.codigo_retirada} - {self.cliente.nome}"

    @property
    def total(self):
        """Calcula a soma total dos itens deste pedido dinamicamente."""
        return sum(item.subtotal for item in self.itens.all())


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"

    @property
    def subtotal(self):
        return self.quantidade * self.produto.preco


class Pagamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('recusado', 'Recusado'),
    ]

    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='pagamento')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    metodo = models.CharField(max_length=50, default='PIX')

    def __str__(self):
        return f"Pagamento Pedido {self.pedido.codigo_retirada} - {self.status}"