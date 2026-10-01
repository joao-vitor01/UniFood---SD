from django.db import models
from cantina.models import Produto

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Recebido')
    codigo_retirada = models.CharField(max_length=10)
    criado_em = models.DateTimeField(auto_now_add=True)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pendente')
    metodo = models.CharField(max_length=50, default='PIX')
    


