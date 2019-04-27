from django.shortcuts import render
from django.views.generic.base import TemplateView
from datetime import datetime
from .models import Uploadxls, Testexls
import xlrd


class Testeup(TemplateView):

    template_name = 'modulopcp/upload.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()

        workbook = xlrd.open_workbook('xls/document4.xls')
        worksheet = workbook.sheet_by_index(0)

        listaxls = []
        for row_num in range(worksheet.nrows):
            row = worksheet.row_values(row_num)
            listaxls.append(row)

        listbulk = []

        for item in listaxls:
            p = Testexls(campo1=item[0], campo2=item[1])
            listbulk.append(p)

        Testexls.objects.update_or_bulk_create(listbulk)

        context['listbulk'] = listaxls

        #Uploadxls.objects.bulk_create(listaxls)



        return context
