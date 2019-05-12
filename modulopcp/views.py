from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import xlrd
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import View, ListView
from .models import Opsv2, Upload_list_opv2, Reg_entregav2
from .forms import Reg_entregaForm
from .utils import render_to_pdf
import io
from django.template.loader import get_template
from xhtml2pdf import pisa


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response
        )
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf'
            )
            response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
            return response
        else:
            return HttpResponse("Erro ao gerar o arquivo", status=400)


class Pdfprod(View):

    def get(self, request):
        ops = Reg_entregav2.objects.all
        now = datetime.now()
        params = {
            'ops': ops,
            'request': request,
            'now': now,
        }

        return Render.render('modulopcp/relatoriopdfprod.html', params, 'Ops_em_producao-{}.pdf'.format(datetime.now().strftime("%d%m%Y")))


@method_decorator(login_required, name='dispatch')
class RelprodPDF(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context['object_list'] = Reg_entregav2.objects.all
        context['now'] = datetime.now()
        pdf = render_to_pdf('pdf/relopsprod.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "OPs em produção - {}.pdf".format(datetime.now().strftime("%d%m%Y"))
            content = "inline; filename={}".format(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename={}".format(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse('Relatorio não encontrado')


@method_decorator(login_required, name='dispatch')
class RelexpedPDF(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context['object_list'] = Reg_entregav2.objects.all
        context['now'] = datetime.now()
        pdf = render_to_pdf('pdf/relopsprod.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "OPs em expedição - {}.pdf".format(datetime.now().strftime("%d%m%Y"))
            content = "inline; filename={}".format(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename={}".format(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse('Relatorio não encontrado')


@method_decorator(login_required, name='dispatch')
class Upload_op(View):

    def get(self, request, *args, **kwargs):

        prompt = {
            'Upload do xml': 'Faça upload para inserir ou atualizar os dados das OPS'
        }
        return render(request, 'modulopcp/uploadop.html', prompt)

    def post(self, request, *args, **kwargs):

        context = {}

        xls_file = request.FILES['file']
        Upload_list_opv2.objects.update_or_create(descricao=xls_file.name, arquivo=xls_file)

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
            Opsv2.objects.update_or_create(
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

            cons = Opsv2.objects.all().order_by("-id")[0]
            Reg_entregav2.objects.update_or_create(op=cons)

        now = datetime.now().strftime("%d-%m-%y as %H:%M:%S")
        messages.success(request, 'Upload realizado com sucesso em: ' + str(now))
        context['listaxls'] = listaxls

        return render(request, 'modulopcp/uploadop.html', context)

"""
@method_decorator(login_required, name='dispatch')
class Novo_reg_entrega(CreateView):

    model = Reg_entrega
    template_name = 'modulopcp/listagemopcomp.html'
    fields = '__all__'
    success_url = reverse_lazy('url_list_prod_comp_op')
"""

@login_required
def upprod(request, pk):

    ent = datetime.now()

    if request.method == 'POST':
        Reg_entregav2.objects.filter(pk=pk).update(produzido=ent)

    return HttpResponse('<script>history.back();</script>')
    #return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def canprod(request, pk):

    if request.method == 'POST':
        Reg_entregav2.objects.filter(pk=pk).update(cancelada=True)

    return HttpResponse('<script>history.back();</script>')


@login_required
def upent(request, pk):

    ent = datetime.now()

    if request.method == 'POST':
        Reg_entregav2.objects.filter(pk=pk).update(entrega=ent)

    return HttpResponse('<script>history.back();</script>')


@method_decorator(login_required, name='dispatch')
class List_prod_comp_op(ListView):

    model = Reg_entregav2
    template_name = 'modulopcp/listagemopcomp.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Reg_entregaForm()
        return context



@method_decorator(login_required, name='dispatch')
class List_prod_op(ListView):

    model = Reg_entregav2
    template_name = 'modulopcp/listagemoppro.html'
    ordering = ['-op']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Reg_entregaForm()
        context['now'] = datetime.now()

        return context


@method_decorator(login_required, name='dispatch')
class List_ent_op(ListView):

    model = Reg_entregav2
    template_name = 'modulopcp/listagemopent.html'
    ordering = ['-op']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Reg_entregaForm()
        context['now'] = datetime.now()
        return context
