from django.contrib import admin
from .models import Categoria, Produto, EstoqueDiario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco')
    list_filter = ('categoria',)
    search_fields = ('nome',)

@admin.register(EstoqueDiario)
class EstoqueDiarioAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data')
    list_filter = ('data', 'produto')