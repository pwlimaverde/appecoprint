from django.db import models


class Upload_list_op(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    arquivo = models.FileField(max_length=200, upload_to='static/arquivosxls/', blank=False, null=False)

    def __str__(self):
        return self.descricao
