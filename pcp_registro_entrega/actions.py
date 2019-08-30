from datetime import datetime


def produzido(modeladmin, request, queryset):
    ent = datetime.now()
    queryset.update(produzido=ent)

produzido.short_description = 'Material Produzido'

def entrega(modeladmin, request, queryset):
    ent = datetime.now()
    queryset.update(entrega=ent)

entrega.short_description = 'Material Entregue'

def mesacacabamento(modeladmin, request, queryset):
    queryset.update(obs="Em mesa de acabamento")

mesacacabamento.short_description = 'Mesa de Acabamento'

def corteevinco(modeladmin, request, queryset):
    queryset.update(obs="Em corte e vinco")

corteevinco.short_description = 'Corte e Vinco'

def laminacao(modeladmin, request, queryset):
    queryset.update(obs="Em laminação")

laminacao.short_description = 'Laminação'

def dobra(modeladmin, request, queryset):
    queryset.update(obs="Em dobradeira")

dobra.short_description = 'Dobradeira'

def colagemm(modeladmin, request, queryset):
    queryset.update(obs="Em colagem manual")

colagemm.short_description = 'Colagem Manual'

def colagemc(modeladmin, request, queryset):
    queryset.update(obs="Em cartucheira")

colagemc.short_description = 'Colagem Cartucheira'

def numeracao(modeladmin, request, queryset):
    queryset.update(obs="Em numeração")

numeracao.short_description = 'Numeração'

def servter(modeladmin, request, queryset):
    queryset.update(obs="Em terceirização")

servter.short_description = 'Terceirização'

