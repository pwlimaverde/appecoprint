from django.shortcuts import render
from django.contrib import messages
from django.views.generic.base import TemplateView
from datetime import datetime
from .models import Uploadxls, Testexls3
import xlrd


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
