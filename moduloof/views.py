from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Orcamento_adesivo, Orcamento_filme
from .forms import OcadesivoForm, OcfilmeForm


# Views
def home(request):
    return render(request, 'moduloof/home.html')


def locadesivo(request):
    data = {}
    listagem = Orcamento_adesivo.objects.all()
    data['listagem'] = listagem
    return render(request, 'moduloof/locadesivo.html', data)


def locfilme(request):
    data = {}
    listagem = Orcamento_filme.objects.all()
    data['listagem'] = listagem
    return render(request, 'moduloof/locfilme.html', data)


def novo_ocadesivo(request):
    data = {}
    form = OcadesivoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_ladesivo')

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


def cons_ocfilme(request, pk):
    data = {}
    cons = Orcamento_filme.objects.get(pk=pk)
    form = OcfilmeForm(request.POST or None, instance=cons)

    if form.is_valid():
        form.save()
        return redirect('url_cons_ocfilme', cons.id)

    # Constantes
    mi = float(6)
    vatmi = int(700)
    conv = int(1000)

    # Dados BD
    larg = float(cons.larg)
    comp = float(cons.comp)
    rend = float(cons.material.rendimento)
    gram = float(cons.material.gramatura)
    va = float(cons.material.valor_de_venda)
    inc = cons.acabamento.incremento
    quant = int(cons.quantidade)

    # Calculos Base
    area = float(round((comp / conv) * (larg / conv), 5))
    kgmi = float(vatmi / (va + mi))
    ar = float(area * rend)
    quantmi = int(round(float((kgmi * float(conv)) / ar), 0))
    quantmi = str(quantmi)

    # Condicional de arredondamento
    if len(quantmi) >= 7:
        unidade = 1000000
    elif len(quantmi) >= 6:
        unidade = 100000
    elif len(quantmi) >= 5:
        unidade = 10000
    elif len(quantmi) >= 4:
        unidade = 1000
    elif len(quantmi) >= 3:
        unidade = 100
    elif len(quantmi) >= 2:
        unidade = 10
    else:
        unidade = 1

    quantmi = (int(quantmi[0]) + 1) * unidade

    if quant < quantmi:
        quanta = quantmi
    else:
        quanta = int(quant * 1)

    quantb = int(quanta * 2)
    quantc = int(quanta * 3)
    mqmi = float((area * rend * quantmi)/conv)
    mqa = float((area * rend * quanta)/conv)
    mqb = float((area * rend * quantb)/conv)
    mqc = float((area * rend * quantc)/conv)

    # Calculos Valores
    vaa = calculovf(mqa, va, inc)
    vab = calculovf(mqb, va, inc)
    vac = calculovf(mqc, va, inc)
    vami = calculovf(mqmi, va, inc)

    if vab >= vaa:
        quantb = quantb * 2
        mqb = float((area * rend * quantb)/conv)
        vab = calculova(mqb, va, inc)
        if vab >= vaa:
            vab = round(calculodes(vaa, 3), 2)

    if vac >= vab:
        quantc = quantb * 2
        mqc = float((area * rend * quantc)/conv)
        vac = calculova(mqc, va, inc)
        if vac >= vab:
            vac = round(calculodes(vab, 3), 2)


    # Valor Unitário
    resa = float(round(((mqa * vaa) / quanta), 4))
    resb = float(round(((mqb * vab) / quantb), 4))
    resc = float(round(((mqc * vac) / quantc), 4))


    data['valor_a'] = resa
    data['total_a'] = round(mqa * vaa, 2)
    data['totalp_a'] = round(mqa, 2)
    data['valor_b'] = resb
    data['total_b'] = round(mqb * vab, 2)
    data['totalp_b'] = round(mqb, 2)
    data['valor_c'] = resc
    data['total_c'] = round(mqc * vac, 2)
    data['totalp_c'] = round(mqc, 2)
    data['quanta'] = quanta
    data['quantb'] = quantb
    data['quantc'] = quantc
    data['vaa'] = vaa
    data['vab'] = vab
    data['vac'] = vac
    data['vami'] = vami
    data['quantmi'] = quantmi
    data['mqa'] = mqa
    data['area'] = area
    data['kgmi'] = kgmi
    data['ar'] = ar

    data['form'] = form
    return render(request, 'moduloof/ocfilme.html', data)
