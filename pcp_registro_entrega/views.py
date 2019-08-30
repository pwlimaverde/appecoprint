from datetime import datetime
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from .models import RegistroEntrega
from .forms import RegistroEntregaForm


@login_required
def upprod(request, pk):

    ent = datetime.now()

    if request.method == 'POST':
        RegistroEntrega.objects.filter(pk=pk).update(produzido=ent)

    return HttpResponse('<script>history.back();</script>')


@login_required
def canprod(request, pk):

    if request.method == 'POST':
        RegistroEntrega.objects.filter(pk=pk).update(cancelada=True)

    return HttpResponse('<script>history.back();</script>')


@login_required
def upent(request, pk):

    ent = datetime.now()

    if request.method == 'POST':
        RegistroEntrega.objects.filter(pk=pk).update(entrega=ent)

    return HttpResponse('<script>history.back();</script>')


@method_decorator(login_required, name='dispatch')
class List_prod_comp_op(ListView):

    model = RegistroEntrega
    template_name = 'pcp_registro_entrega/listagemopcomp.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistroEntregaForm()
        return context


@method_decorator(login_required, name='dispatch')
class List_prod_op(ListView):

    model = RegistroEntrega
    template_name = 'pcp_registro_entrega/listagemoppro.html'
    ordering = ['-op']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistroEntregaForm()
        context['now'] = datetime.now()

        return context


@method_decorator(login_required, name='dispatch')
class List_ent_op(ListView):

    model = RegistroEntrega
    template_name = 'pcp_registro_entrega/listagemopent.html'
    ordering = ['-op']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistroEntregaForm()
        context['now'] = datetime.now()
        return context
