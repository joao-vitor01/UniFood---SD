import re
from django.db import models
from django.core.exceptions import ValidationError

from cantina.models import Produto

def validar_cpf(valor):
    # Remove qualquer caractere que não seja número (pontos, traços)
    cpf = re.sub(r'[^0-9]', '', str(valor))
    
    # Verifica se tem 11 dígitos ou se são todos números iguais (ex: 111.111.111-11)
    if len(cpf) != 11 or len(set(cpf)) == 1:
        raise ValidationError('CPF inválido.')
    
    # Algoritmo matemático para validar os dois dígitos verificadores do CPF
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            raise ValidationError('CPF inválido.')


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Recebido')
    codigo_retirada = models.CharField(max_length=10)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"

class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pendente')
    metodo = models.CharField(max_length=50, default='PIX')

    def __str__(self):
        return f"Pagamento Pedido #{self.pedido.id} - {self.status}"