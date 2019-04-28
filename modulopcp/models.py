from django.db import models


class Uploadxls(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    arquivo = models.FileField(max_length=200, upload_to='xls/')


class Testexls3(models.Model):
    campo1 = models.CharField(max_length=200)
    campo2 = models.CharField(max_length=200)

    def __str__(self):
        return self.campo1 + ' - ' + self.campo2

