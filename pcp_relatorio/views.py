from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
import io
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime
from pcp_registro_entrega.models import RegistroEntrega
from pcp_registro_entrega.forms import RegistroEntregaForm


@method_decorator(login_required, name='dispatch')
class Impprod(ListView):
    model = RegistroEntrega
    template_name = 'pcp_relatorio/impprod.html'
    ordering = ['-op']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistroEntregaForm()
        context['now'] = datetime.now()

        return context


@method_decorator(login_required, name='dispatch')
class Impexped(ListView):
    model = RegistroEntrega
    template_name = 'pcp_relatorio/impexped.html'
    ordering = ['-op']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistroEntregaForm()
        context['now'] = datetime.now()

        return context


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


@method_decorator(login_required, name='dispatch')
class Pdfprod(View):

    def get(self, request):
        ops = RegistroEntrega.objects.all
        now = datetime.now()
        params = {
            'ops': ops,
            'request': request,
            'now': now,
        }

        return Render.render('pcp_relatorio/relatoriopdfprod.html', params, 'Ops_em_producao-{}.pdf'.format(datetime.now().strftime("%d%m%Y")))


@method_decorator(login_required, name='dispatch')
class Pdfexped(View):

    def get(self, request):
        ops = RegistroEntrega.objects.all
        now = datetime.now()
        params = {
            'ops': ops,
            'request': request,
            'now': now,
        }

        return Render.render('pcp_relatorio/relatoriopdfexped.html', params, 'Ops_em_expedicao-{}.pdf'.format(datetime.now().strftime("%d%m%Y")))
