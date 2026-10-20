from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class EstoqueDiario(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} un."