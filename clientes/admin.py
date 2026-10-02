from django.contrib import admin
from .models import Cliente, Pedido, ItemPedido, Pagamento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'email')
    search_fields = ('nome', 'matricula', 'email')

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0

class PagamentoInline(admin.StackedInline):
    model = Pagamento
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'status', 'codigo_retirada', 'criado_em')
    list_filter = ('status', 'criado_em')
    search_fields = ('cliente__nome', 'codigo_retirada', 'cliente__matricula')
    inlines = [ItemPedidoInline, PagamentoInline]

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'status', 'metodo')
    list_filter = ('status', 'metodo')