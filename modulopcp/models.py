from django.db import models
from datetime import datetime

class Upload_list_opv2(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    arquivo = models.FileField(max_length=200, upload_to='static/arquivosxls/', blank=False, null=False)

    def __str__(self):
        return self.descricao

class Opsv2(models.Model):
    orcamento = models.IntegerField(max_length=5, blank=False, null=False)
    cliente = models.CharField(max_length=300, blank=False, null=False)
    servico = models.TextField(blank=False, null=False)
    quant = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    entrada = models.DateField(blank=False, null=False)
    vendedor = models.CharField(max_length=100, blank=False, null=False)
    op = models.IntegerField(max_length=5, blank=False, null=False)
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
            stat['posicao'] = 'Atrazado a ' + str(sdiasat[0]) + ' dia(s)'
        elif sepe[0] == sepn[0]:
            stat['posicao'] = 'Entrega Hoje'
        elif diasp[0] <= '1':
            stat['posicao'] = 'Entrega Amanhã'
        else:
            stat['posicao'] = 'Entrega em ' + str(sdias[0]) + ' dias'

        return stat

    def __str__(self):
        return str(self.op) + ' - ' + self.cliente


class Reg_entregav2(models.Model):
    op = models.OneToOneField(Opsv2, on_delete=models.PROTECT, blank=False, null=False)
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

        return str(self.op) + ' - ' + str(self.produzido)
