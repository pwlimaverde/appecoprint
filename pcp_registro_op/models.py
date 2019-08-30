from django.db import models
from datetime import datetime


class RegistroOp(models.Model):
    orcamento = models.IntegerField(blank=False, null=False)
    cliente = models.CharField(max_length=300, blank=False, null=False)
    servico = models.TextField(blank=False, null=False)
    quant = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    entrada = models.DateField(blank=False, null=False)
    vendedor = models.CharField(max_length=100, blank=False, null=False)
    op = models.IntegerField(blank=False, null=False)
    prev_entrega = models.DateTimeField(blank=False, null=False)

    def status(self):
        stat = {}
        now = str(datetime.now())
        ent = str(self.prev_entrega)
        sepe = ent.split(' ')
        sepn = now.split(' ')
        dpe = datetime.strptime(sepe[0], '%Y-%m-%d').date()
        dpn = datetime.strptime(sepn[0], '%Y-%m-%d').date()
        diasp = str(dpe - dpn)
        diasat = str(dpn - dpe)
        sdias = diasp.split(' ')
        sdiasat = diasat.split(' ')
        if sdias[0] == '0:00:00':
            stat['diasp'] = 0
        else:
            stat['diasp'] = int(sdias[0])

        if sepe[0] < sepn[0]:
            stat['posicao'] = 'Atrasado a ' + str(sdiasat[0]) + ' dia(s)'
        elif sepe[0] == sepn[0]:
            stat['posicao'] = 'Entrega Hoje'
        elif diasp[0] <= '1':
            stat['posicao'] = 'Entrega Amanhã'
        else:
            stat['posicao'] = 'Entrega em ' + str(sdias[0]) + ' dias'

        return stat

    def __str__(self):
        return str(self.op) + ' - ' + self.cliente