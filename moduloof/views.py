from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Orcamento_adesivo, Orcamento_filme
from .forms import OcadesivoForm, OcfilmeForm



# Views

@method_decorator(login_required, name='dispatch')
class Cadastro(TemplateView):

    template_name = 'moduloof/cadastro.html'


@method_decorator(login_required, name='dispatch')
class Novo_ocadesivo(CreateView):

    model = Orcamento_adesivo
    template_name = 'moduloof/orcadesivo.html'
    fields = '__all__'
    success_url = reverse_lazy('url_ladesivo')

"""
@login_required
def duporcadesivo(request, pk):
    data = {}
    cons = Orcamento_adesivo.objects.get(pk=pk)
    if request.method == 'POST':
        form = OcadesivoForm(request.POST or None)

        if form.is_valid():
            form.save()
            cons = Orcamento_adesivo.objects.all().order_by("-id")[0]
            return redirect('url_cons_ocadesivo', cons.id)

        data['form'] = form
        return render(request, 'moduloof/orcadesivo.html', data)


    else:

        form = OcadesivoForm(request.POST or None, instance=cons)
        data['form'] = form

    return render(request, 'moduloof/duporcadesivo.html', data)
"""

@method_decorator(login_required, name='dispatch')
class Locadesivo(ListView):

    model = Orcamento_adesivo
    template_name = 'moduloof/lorcadesivo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OcadesivoForm()
        return context


@method_decorator(login_required, name='dispatch')
class Cons_ocadesivo(UpdateView):

    model = Orcamento_adesivo
    template_name = 'moduloof/orcadesivo.html'
    fields = '__all__'

    def get_success_url(self):
        # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
        companyid = self.kwargs['pk']
        return reverse_lazy('url_cons_ocadesivo', kwargs={'pk': companyid})

"""
@login_required
def cons_ocadesivo(request, pk):
    data = {}
    cons = Orcamento_adesivo.objects.get(pk=pk)
    form = OcadesivoForm(request.POST or None, instance=cons)

    if form.is_valid():
        form.save()
        return redirect('url_cons_ocadesivo', cons.id)

    data['vaa'] = cons.vaa
    data['mqa'] = cons.mqa
    data['valor_a'] = cons.resa
    data['total_a'] = cons.total_a
    data['quanta'] = cons.quanta

    data['vab'] = cons.vab
    data['mqb'] = cons.mqb
    data['valor_b'] = cons.resb
    data['total_b'] = cons.total_b
    data['quantb'] = cons.quantb

    data['vac'] = cons.vac
    data['mqc'] = cons.mqc
    data['valor_c'] = cons.resc
    data['total_c'] = cons.total_c
    data['quantc'] = cons.quantc

    data['quantmi'] = cons.quantmi

    data['cadastro'] = cons
    data['form'] = form
    return render(request, 'moduloof/orcadesivo.html', data)

"""

@method_decorator(login_required, name='dispatch')
class Novo_ocfilme(CreateView):

    model = Orcamento_filme
    template_name = 'moduloof/orcfilme.html'
    fields = '__all__'
    success_url = reverse_lazy('url_lfilme')


@login_required
def duporcfilme(request, pk):
    data = {}
    cons = Orcamento_filme.objects.get(pk=pk)
    if request.method == 'POST':
        form = OcfilmeForm(request.POST or None)

        if form.is_valid():
            form.save()
            cons = Orcamento_filme.objects.all().order_by("-id")[0]
            return redirect('url_cons_ocfilme', cons.id)

        data['form'] = form
        return render(request, 'moduloof/orcfilme.html', data)


    else:

        form = OcfilmeForm(request.POST or None, instance=cons)
        data['form'] = form

    return render(request, 'moduloof/duporcfilme.html', data)


@method_decorator(login_required, name='dispatch')
class Locfilme(ListView):

    model = Orcamento_filme
    template_name = 'moduloof/lorcfilme.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OcfilmeForm()
        return context


@login_required
def cons_ocfilme(request, pk):
    data = {}
    cons = Orcamento_filme.objects.get(pk=pk)
    form = OcfilmeForm(request.POST or None, instance=cons)

    if form.is_valid():
        form.save()
        return redirect('url_cons_ocfilme', cons.id)

    data['mqa'] = cons.mqa
    data['area'] = cons.area
    data['ar'] = cons.ar

    data['vami'] = cons.vami
    data['kgmi'] = cons.kgmi
    data['quantmi'] = cons.quantmi

    data['vaa'] = cons.vaa
    data['quanta'] = cons.quanta
    data['valor_a'] = cons.valor_a
    data['total_a'] = cons.total_a
    data['totalp_a'] = cons.totalp_a

    data['vab'] = cons.vab
    data['quantb'] = cons.quantb
    data['valor_b'] = cons.valor_b
    data['total_b'] = cons.total_b
    data['totalp_b'] = cons.totalp_b

    data['vac'] = cons.vac
    data['valor_c'] = cons.valor_c
    data['quantc'] = cons.quantc
    data['total_c'] = cons.total_c
    data['totalp_c'] = cons.totalp_c

    data['cadastro'] = cons
    data['form'] = form
    return render(request, 'moduloof/orcfilme.html', data)
