from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import xlrd
from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from .models import Upload_list_op
from pcp_registro_op.models import RegistroOp
from pcp_registro_entrega.models import RegistroEntrega


@method_decorator(login_required, name='dispatch')
class Upload_op(View):

    def get(self, request, *args, **kwargs):

        prompt = {
            'Upload do xml': 'Faça upload para inserir ou atualizar os dados das OPS'
        }
        return render(request, 'pcp_upload_xls/uploadop.html', prompt)

    def post(self, request, *args, **kwargs):

        context = {}

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
            RegistroOp.objects.update_or_create(
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

            cons = RegistroOp.objects.all().order_by("-id")[0]
            RegistroEntrega.objects.update_or_create(op=cons)

        now = datetime.now().strftime("%d-%m-%y as %H:%M:%S")
        messages.success(request, 'Upload realizado com sucesso em: ' + str(now))
        context['listaxls'] = listaxls

        return render(request, 'pcp_upload_xls/uploadop.html', context)
