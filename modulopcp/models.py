from django.db import models


class Cont_op(models.Model):
    op = models.CharField(max_length=200, blank=False, null=False)
    servico = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.op + ' - ' + self.servico