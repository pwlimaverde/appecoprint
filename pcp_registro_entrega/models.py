from django.db import models
from datetime import datetime
from pcp_registro_op.models import RegistroOp


class RegistroEntrega(models.Model):
    op = models.OneToOneField(RegistroOp, on_delete=models.PROTECT, blank=False, null=False)
    produzido = models.DateField(blank=True, null=True)
    obs = models.CharField(max_length=50, blank=True, null=True)
    entrega = models.DateField(blank=True, null=True)
    cancelada = models.BooleanField(default=False)

    def statusent(self):
        statent = {}
        now = str(datetime.now())
        prod = str(self.produzido)
        sepe = prod.split(' ')
        sepn = now.split(' ')
        dpe = datetime.strptime(sepe[0], '%Y-%m-%d').date()
        dpn = datetime.strptime(sepn[0], '%Y-%m-%d').date()
        diasp = str(dpe - dpn)
        diasat = str(dpn - dpe)
        sdias = diasp.split(' ')
        sdiasat = diasat.split(' ')
        if sdias[0] == '0:00:00':
            statent['diasat'] = 0
        else:
            statent['diasat'] = int(sdiasat[0])


        if sepe[0] < sepn[0]:
            statent['posicao'] = 'Em expedição a ' + str(sdiasat[0]) + ' dias'
        elif sepe[0] == sepn[0]:
            statent['posicao'] = 'Entrou em expedição Hoje'

        return statent

    def __str__(self):

        if self.cancelada == True:
            return str(self.op) + ' - ' + str(self.entrega) + ' - Cancelada'
        else:
            return str(self.op) + ' - ' + str(self.produzido)
