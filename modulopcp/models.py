from django.db import models


class Uploadxls(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    arquivo = models.FileField(max_length=200, upload_to='xls/')


class Testexls3(models.Model):
    campo1 = models.CharField(max_length=200)
    campo2 = models.CharField(max_length=200)

    def __str__(self):
        return self.campo1 + ' - ' + self.campo2


class Upload_list_op(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    arquivo = models.FileField(max_length=200, upload_to='static/arquivosxls/', blank=False, null=False)


class Ops(models.Model):
    orcamento = models.IntegerField(max_length=5, blank=False, null=False)
    cliente = models.CharField(max_length=300, blank=False, null=False)
    servico = models.TextField(blank=False, null=False)
    quant = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    entrada = models.DateField()
    vendedor = models.CharField(max_length=100, blank=False, null=False)
    op = models.IntegerField(max_length=5, blank=False, null=False)
    prev_entrega = models.DateTimeField()

    def __str__(self):
        return str(self.orcamento) + ' - ' + self.cliente



