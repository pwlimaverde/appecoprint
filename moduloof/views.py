from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
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


@login_required
def novo_ocadesivo(request):
    data = {}
    form = OcadesivoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_ladesivo')

    data['form'] = form
    return render(request, 'moduloof/orcadesivo.html', data)


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


@login_required
def locadesivo(request):
    data = {}
    form = OcadesivoForm()
    listagem = Orcamento_adesivo.objects.all()

    data['listagem'] = listagem
    data['form'] = form
    return render(request, 'moduloof/lorcadesivo.html', data)


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


@login_required
def novo_ocfilme(request):
    data = {}
    form = OcfilmeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_lfilme')

    data['form'] = form
    return render(request, 'moduloof/orcfilme.html', data)


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


@login_required
def locfilme(request):
    data = {}
    form = OcfilmeForm()
    listagem = Orcamento_filme.objects.all()
    data['listagem'] = listagem
    data['form'] = form
    return render(request, 'moduloof/lorcfilme.html', data)


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
