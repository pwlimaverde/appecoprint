from django.contrib import admin
from .actions import corteevinco, laminacao,  colagemm, colagemc, numeracao, servter, dobra, produzido, entrega
from .models import Upload_list_opv2, Opsv2, Reg_entregav2


class Opsv2Admin(admin.ModelAdmin):
    fields = (('op', 'orcamento', 'quant'), ('cliente', 'vendedor'), ('servico'), ('entrada'), ('prev_entrega'))
    list_display = ('op', 'quant', 'cliente', 'vendedor', 'servico', 'entrada', 'prev_entrega')
    list_filter = ('vendedor', 'cliente')
    search_fields = ('op', 'orcamento', 'cliente', 'vendedor', 'servico')


class Reg_entregav2Admin(admin.ModelAdmin):
    list_display = ('opd', 'servico', 'prev_entrega', 'produzido', 'entrega', 'obs', 'canceladad')
    list_filter = ('op__prev_entrega', 'obs')
    search_fields = ('op__op', 'op__cliente', 'op__servico',)
    actions = [produzido, entrega, corteevinco, laminacao, dobra, colagemm, colagemc, numeracao, servter]

    def opd(self, obj):
        opd = str(obj.op)
        return opd[0:40]

    opd.short_description = 'op'

    def servico(self, obj):
        serv = obj.op.servico
        return serv[0:80]

    servico.short_description = 'serviço'

    def prev_entrega(self, obj):
        prev_entrega = obj.op.prev_entrega
        return prev_entrega

    prev_entrega.short_description = 'prev. entrega'

    def canceladad(self, obj):

        if obj.cancelada:
            return 'cancelada'
        else:
            return ''

    canceladad.short_description = ''


admin.site.register(Upload_list_opv2)
admin.site.register(Opsv2, Opsv2Admin)
admin.site.register(Reg_entregav2, Reg_entregav2Admin)
