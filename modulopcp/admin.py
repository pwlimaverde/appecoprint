from django.contrib import admin
from .models import Upload_list_opv2, Opsv2, Reg_entregav2

class Opsv2Admin(admin.ModelAdmin):
    fields = (('op', 'orcamento', 'quant'), ('cliente', 'vendedor'),('servico'),('entrada'), ('prev_entrega'))
    list_display = ('op', 'quant', 'cliente', 'vendedor', 'servico', 'entrada', 'prev_entrega')
    list_filter = ('vendedor', 'cliente')


class Reg_entregav2Admin(admin.ModelAdmin):
    list_display = ('op', 'produzido', 'entrega', 'cancelada')
    list_filter = ('op__prev_entrega', 'produzido')

admin.site.register(Upload_list_opv2)
admin.site.register(Opsv2, Opsv2Admin)
admin.site.register(Reg_entregav2, Reg_entregav2Admin)
