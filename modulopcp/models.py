from django.db import models


class Relacao_op(models.Model):
    oc = models.IntegerField(max_length=5, blank=False, null=False)
    cliente = models.CharField(max_length=300, blank=False, null=False)
    servico = models.CharField(max_length=400, blank=False, null=False)
    quant = models.IntegerField(max_length=8, blank=False, null=False)
    valor = models.DecimalField(max_digits=8, decimal_places=4, blank=False, null=False)
    entrada = models.CharField(max_length=400, blank=False, null=False)
    vendedor = models.CharField(max_length=200, blank=False, null=False)
    op = models.CharField(max_length=200, blank=False, null=False)
    prev_entrega = models.CharField(max_length=400, blank=False, null=False)
    nota = models.CharField(max_length=200, blank=False, null=False)
    entrega = models.CharField(max_length=400, blank=False, null=False)
    obs = models.TextField(blank=True, null=True)
    finalizada = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.op + ' - ' + self.servico