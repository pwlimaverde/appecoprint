from django.db import models


class Upload_list_op(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    arquivo = models.FileField(max_length=200, upload_to='static/arquivosxls/', blank=False, null=False)

    def __str__(self):
        return self.descricao

class Ops(models.Model):
    orcamento = models.IntegerField(max_length=5, blank=False, null=False)
    cliente = models.CharField(max_length=300, blank=False, null=False)
    servico = models.TextField(blank=False, null=False)
    quant = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    entrada = models.DateField(blank=False, null=False)
    vendedor = models.CharField(max_length=100, blank=False, null=False)
    op = models.IntegerField(max_length=5, blank=False, null=False)
    prev_entrega = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return str(self.prev_entrega) + ' - ' + self.cliente


class Reg_entrega(models.Model):
    op = models.OneToOneField(Ops, on_delete=models.PROTECT, blank=False, null=False)
    entrega = models.DateField(blank=True, null=True)
    cancelada = models.BooleanField(default=False)

    def __str__(self):

        if self.cancelada == True:
            return str(self.op) + ' - ' + str(self.entrega) + ' - Cancelada'

        return str(self.op) + ' - ' + str(self.entrega)
