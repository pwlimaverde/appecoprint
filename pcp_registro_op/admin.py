from django.contrib import admin
from .models import RegistroOp


class RegistroOpAdmin(admin.ModelAdmin):
    fields = (('op', 'orcamento', 'quant'), ('cliente', 'vendedor'), ('servico'), ('entrada'), ('prev_entrega'))
    list_display = ('op', 'quant', 'cliente', 'vendedor', 'servico', 'entrada', 'prev_entrega')
    list_filter = ('vendedor', 'cliente')
    search_fields = ('op', 'orcamento', 'cliente', 'vendedor', 'servico')


admin.site.register(RegistroOp, RegistroOpAdmin)