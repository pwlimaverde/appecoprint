import csv, io
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from datetime import datetime
from .models import Cont_op


class Home_website(TemplateView):

    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


@login_required
def uploadop(request):

    prompt = {
        'order': 'Order of the CSV should be op, servico'
    }

    if request.method == 'GET':
        return render(request, 'website/uploadop.html', prompt)

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

    return render(request, 'website/uploadop.html', context)
