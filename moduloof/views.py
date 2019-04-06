from django.shortcuts import render, redirect
from .models import Orcamento_adesivo, Orcamento_filme
from .forms import OcadesivoForm, OcfilmeForm


# Views
def home(request):
    return render(request, 'moduloof/home.html')


def novo_ocadesivo(request):
    data = {}
    form = OcadesivoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_ladesivo')

    data['form'] = form
    return render(request, 'moduloof/ocadesivo.html', data)


def locadesivo(request):
    data = {}
    listagem = Orcamento_adesivo.objects.all()
    data['listagem'] = listagem
    return render(request, 'moduloof/locadesivo.html', data)


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

    data['form'] = form
    return render(request, 'moduloof/ocadesivo.html', data)


def novo_ocfilme(request):
    data = {}
    form = OcfilmeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_lfilme')

    data['form'] = form
    return render(request, 'moduloof/ocfilme.html', data)


def locfilme(request):
    data = {}
    listagem = Orcamento_filme.objects.all()
    data['listagem'] = listagem
    return render(request, 'moduloof/locfilme.html', data)


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

    data['form'] = form
    return render(request, 'moduloof/ocfilme.html', data)
