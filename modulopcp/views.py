import csv, io
from django.contrib import messages
from .models import Cont_op
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView


class Import(TemplateView):

    template_name = 'modulopcp/import.html'


@login_required
def uploadop(request):

    prompt = {
        'order': 'Order of the CSV should be op, servico'
    }

    if request.method == 'GET':
        return render(request, 'modulopcp/uploadop.html', prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Upload apenas de arquivos CSV')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Cont_op.objects.update_or_create(
            op=column[0],
            servico=column[1]
        )
    context = {}

    return render(request, 'modulopcp/uploadop.html', context)