from django.shortcuts import render
from django.contrib import messages
from django.views.generic.base import TemplateView, View
from datetime import datetime
from .models import Uploadxls, Testexls3, Ops, Upload_list_op
import xlrd


class Upload_op(View):

    def get(self, request, *args, **kwargs):

        prompt = {
            'Upload do xml': 'Faça upload para inserir ou atualizar os dados'
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
            #row[8] = datetime(*xlrd.xldate_as_tuple(row[8], datemode))
            listaxls.append(row)

        for item in listaxls:
            Ops.objects.update_or_create(
                orcamento=item[0],
                cliente=item[1],
                servico=item[2],
                quant=item[3],
                valor=item[4],
                entrada=item[5],
            )

        context = {}

        context['listaxls'] = listaxls
        context['now'] = datetime.now()

        return render(request, 'modulopcp/uploadop.html', context)



class Testeup(View):
# modelo class view com update or create direto do arquivo
    def get(self, request, *args, **kwargs):

        prompt = {
            'Upload do xml': 'Faça upload para inserir ou atualizar os dados'
        }
        return render(request, 'modulopcp/upload.html', prompt)

    def post(self, request, *args, **kwargs):

        xls_file = request.FILES['file']
        Uploadxls.objects.update_or_create(descricao=xls_file.name, arquivo=xls_file)

        caminho = 'static/arquivosxls/'+xls_file.name

        if not xls_file.name.endswith('.xls'):
            messages.error(request, 'Não é um xml')

        workbook = xlrd.open_workbook(caminho)
        worksheet = workbook.sheet_by_index(0)

        listaxls = []

        for row_num in range(worksheet.nrows):
            row = worksheet.row_values(row_num)
            listaxls.append(row)

        for item in listaxls:
            Testexls3.objects.update_or_create(campo1=item[0], campo2=item[1])

        context = {}

        context['listaxls'] = listaxls
        context['now'] = datetime.now()

        return render(request, 'modulopcp/upload.html', context)



"""
# modelo def com update or create direto do arquivo
def testeup(request):
    template = 'modulopcp/upload.html'

    prompt = {
        'Upload do xml': 'Faça upload para inserir ou atualizar os dados'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    xls_file = request.FILES['file']
    Uploadxls.objects.update_or_create(descricao=xls_file.name, arquivo=xls_file)

    caminho = 'xls/'+xls_file.name

    if not xls_file.name.endswith('.xls'):
        messages.error(request, 'Não é um xml')

    workbook = xlrd.open_workbook(caminho)
    worksheet = workbook.sheet_by_index(0)

    listaxls = []

    for row_num in range(worksheet.nrows):
        row = worksheet.row_values(row_num)
        listaxls.append(row)

    for item in listaxls:
        Testexls3.objects.update_or_create(campo1=item[0], campo2=item[1])

    context = {}

    context['listaxls'] = listaxls
    context['now'] = datetime.now()

    return render(request, template, context)

"""
"""
# modelo update or create
class Testeup(TemplateView):

    template_name = 'modulopcp/upload.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()

        workbook = xlrd.open_workbook('xls/document8.xls')
        worksheet = workbook.sheet_by_index(0)

        listaxls = []

        for row_num in range(worksheet.nrows):
            row = worksheet.row_values(row_num)
            listaxls.append(row)

        listbulk = []

        for item in listaxls:
            p = Testexls3(campo1=item[0], campo2=item[1])
            listbulk.append(p)
            Testexls3.objects.update_or_create(campo1=item[0], campo2=item[1])

        context['listbulk'] = listaxls

        return context
"""
"""
# modelo bulk create
class Testeup(TemplateView):

    template_name = 'modulopcp/upload.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()

        workbook = xlrd.open_workbook('xls/document6.xls')
        worksheet = workbook.sheet_by_index(0)

        listaxls = []
        for row_num in range(worksheet.nrows):
            row = worksheet.row_values(row_num)
            listaxls.append(row)

        listbulk = []

        for item in listaxls:
            p = Testexls3(campo1=item[0], campo2=item[1])
            listbulk.append(p)

        context['listbulk'] = listaxls

        Testexls3.objects.bulk_create(listbulk)

        return context
"""
