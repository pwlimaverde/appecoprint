from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import xlrd
from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from django.views.generic.base import View
from .models import Ops, Upload_list_op


@method_decorator(login_required, name='dispatch')
class Upload_op(View):

    def get(self, request, *args, **kwargs):

        prompt = {
            'Upload do xml': 'Faça upload para inserir ou atualizar os dados das OPS'
        }
        return render(request, 'modulopcp/uploadop.html', prompt)

    def post(self, request, *args, **kwargs):

        xls_file = request.FILES['file']
        Upload_list_op.objects.update_or_create(descricao=xls_file.name, arquivo=xls_file)

        caminho = 'static/arquivosxls/'+xls_file.name

        if not xls_file.name.endswith('.xls'):
            messages.error(request, 'Não é um xml')

        workbook = xlrd.open_workbook(caminho)
        worksheet = workbook.sheet_by_index(0)
        datemode = workbook.datemode

        listaxls = []

        for row_num in range(worksheet.nrows):
            row = worksheet.row_values(row_num)
            row[5] = datetime(*xlrd.xldate_as_tuple(row[5], datemode))
            row[8] = datetime(*xlrd.xldate_as_tuple(row[8], datemode))
            listaxls.append(row)

        for item in listaxls:
            Ops.objects.update_or_create(
                orcamento=item[0],
                cliente=item[1],
                servico=item[2],
                quant=item[3],
                valor=item[4],
                entrada=item[5],
                vendedor=item[6],
                op=item[7],
                prev_entrega=item[8],
            )

        now = datetime.now().strftime("%d-%m-%y as %H:%M:%S")
        messages.success(request, 'Upload realizado com sucesso em: ' + str(now))
        context = {}

        context['listaxls'] = listaxls

        return render(request, 'modulopcp/uploadop.html', context)


