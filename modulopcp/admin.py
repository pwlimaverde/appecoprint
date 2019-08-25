from django.contrib import admin
from .models import Upload_list_opv2, Opsv2, Reg_entregav2


class Opsv2Admin(admin.ModelAdmin):
    fields = (('op', 'orcamento', 'quant'), ('cliente', 'vendedor'), ('servico'), ('entrada'), ('prev_entrega'))
    list_display = ('op', 'quant', 'cliente', 'vendedor', 'servico', 'entrada', 'prev_entrega')
    list_filter = ('vendedor', 'cliente')
    search_fields = ('op', 'orcamento', 'cliente', 'vendedor', 'servico')


class Reg_entregav2Admin(admin.ModelAdmin):
    list_display = ('opd', 'servico', 'produzido', 'entrega', 'canceladad')
    list_filter = ('op__prev_entrega', 'produzido')
    search_fields = ('op__op', 'op__cliente', 'op__servico',)

    def opd(self, obj):
        opd = str(obj.op)
        return opd[0:40]

    opd.short_description = 'op'

    def servico(self, obj):
        serv = obj.op.servico
        return serv[0:80]

    servico.short_description = 'serviço'

    def canceladad(self, obj):

        if obj.cancelada:
            return 'cancelada'
        else:
            return ''

    canceladad.short_description = ''


admin.site.register(Upload_list_opv2)
admin.site.register(Opsv2, Opsv2Admin)
admin.site.register(Reg_entregav2, Reg_entregav2Admin)
