from django.contrib import admin
from .actions import *
from .models import RegistroEntrega


class RegistroEntregaAdmin(admin.ModelAdmin):
    list_display = ('opd', 'servico', 'prev_entrega', 'produzido', 'entrega', 'obs', 'canceladad')
    list_filter = ('op__prev_entrega', 'obs', 'cancelada')
    search_fields = ('op__op', 'op__cliente', 'op__servico',)
    actions = [produzido, entrega, mesacacabamento, corteevinco, laminacao, dobra, colagemm, colagemc, numeracao, servter]

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


admin.site.register(RegistroEntrega, RegistroEntregaAdmin)
