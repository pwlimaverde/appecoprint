from django.shortcuts import render
from django.views.generic.base import TemplateView
from datetime import datetime
from .models import Uploadxls, Testexls3
import xlrd


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
