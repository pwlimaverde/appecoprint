from tkinter import CASCADE

from django.db import models

#Variaveis globais
global x, dva
dva = {}
x = 10

# Metodos
# Adesivio
class calculo(object):

    def calcarea(self, comp, larg):
        conv = 1000
        return float((comp / conv) * (larg / conv))

    def calculodes(self, vl, ac):
        vl = float(vl)
        ac = float(ac)
        if ac > 0:
            return float(vl - (vl * (ac / 100)))
        else:
            return vl

    def calculoaca(self, vl, ac):
        vl = float(vl)
        ac = float(ac)
        if ac > 0:
            return float(vl + (vl * (ac / 100)))
        else:
            return float(vl)

    def calculova(self, mqg, vg):
        # Constantes
        mqg = float(mqg)
        vg = float(vg)
        mi = float(7)
        a = float(5)
        b = float(3)
        c = float(2)
        d = float(1)
        e = float(0)
        ma = float(80)
        mb = float(100)
        mc = float(200)
        md = float(300)
        me = float(350)

        # Calculos Valores do metro
        if mqg >= me:
            return float(vg + e)
        elif mqg >= md:
            return float(vg + d)
        elif mqg >= mc:
            return float(vg + c)
        elif mqg >= mb:
            return float(vg + b)
        elif mqg >= ma:
            return float(vg + a)
        else:
            return float(vg + mi)

    def calc_mq(self, larg, comp, va, quant):
        dmq = {}
        # Constantes
        mi = int(7)
        vatmi = int(700)

        # Dados BD
        larg = float(larg)
        comp = float(comp)
        va = float(va)
        quant = int(quant)

        # Calculos Base
        area = calculo.calcarea(self, comp, larg)
        quantmi = int(vatmi / (area * (va + mi)))
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
            quanta = quant

        dmq['quant'] = quanta
        dmq['quantmi'] = quantmi
        dmq['mq'] = int(area * quanta)
        return dmq


# classes
class Cliente(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    responsavel = models.CharField(max_length=200, blank=False, null=False)
    telefone = models.CharField(max_length=12, blank=False, null=False)

    def __str__(self):
        return self.nome


class Tpfilme(models.Model):
    tipo = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.tipo


class Tpadesivo(models.Model):
    tipo = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.tipo


class Filme_bopp(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    tipo = models.ForeignKey(Tpfilme, on_delete=models.CASCADE, blank=False, null=False)
    micragem = models.DecimalField(max_digits=2, decimal_places=0, blank=False, null=False)
    gramatura = models.DecimalField(max_digits=3, decimal_places=1, blank=False, null=False)
    rendimento = models.DecimalField(max_digits=3, decimal_places=1, blank=False, null=False)
    valor_de_venda = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.descricao


class Acabamento(models.Model):
    tipo = models.CharField(max_length=200, blank=False, null=False)
    incremento = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)

    def __str__(self):
        return self.tipo


class Orcamento_filme(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False)
    servico = models.CharField(max_length=400, blank=False, null=False)
    material = models.ForeignKey(Filme_bopp, on_delete=models.CASCADE, blank=False, null=False)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.CASCADE, blank=False, null=False)
    comp = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)
    larg = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)
    quantidade = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)

    def __str__(self):
        return self.cliente.nome + ' - ' + self.servico


class Adesivo(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    tipo = models.ForeignKey(Tpadesivo, on_delete=CASCADE, blank=False, null=False)
    valor_de_venda = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao


class Orc_adesivo(models.Model, calculo):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False)
    servico = models.CharField(max_length=400, blank=False, null=False)
    material = models.ForeignKey(Adesivo, on_delete=models.CASCADE, blank=False, null=False)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.CASCADE, blank=False, null=False)
    comp = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)
    larg = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)
    quantidade = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)


    def vaa(self):
        # varbd
        comp = self.comp
        larg = self.larg
        inc = float(self.acabamento.incremento)
        va = float(self.material.valor_de_venda)
        quant = float(self.quantidade)

        # geral calc
        area = calculo.calcarea(self, comp, larg)

        # vaa calc
        mqa = calculo.calc_mq(self, larg, comp, va, quant)
        dva['quant'] = quant
        mqq = mqa['mq']
        vaa = calculo.calculova(self, mqq, va)
        dva['vaa'] = calculo.calculoaca(self, vaa, inc)
        return dva['vaa']

    def resa(self, vaa):
        area = area
        dva['resa'] = float(round((area * vaa), 4))
        dva['quantmi'] = mqa['quantmi']
        dva['quanta'] = mqa['quant']

        # vami calc
        quantmi = mqa['quantmi']
        mqmi = calculo.calc_mq(self, larg, comp, va, quantmi)
        mqq = mqmi['mq']
        vami = calculo.calculova(self, mqq, va)
        dva['vami'] = calculo.calculoaca(self, vami, inc)

        # vab calc
        mqb = calculo.calc_mq(self, larg, comp, va, quant * 2)
        mqq = mqb['mq']
        vab = calculo.calculova(self, mqq, va)

        if vab >= vaa:
            mqb = calculo.calc_mq(self, larg, comp, va, quant * 4)
            mqq = mqb['mq']
            vab = calculo.calculova(self, mqq, va)
            if vab >= vaa:
                vab = round(calculo.calculodes(vaa, 3), 2)

        dva['vab'] = calculo.calculoaca(self, vab, inc)
        dva['resb'] = float(round((area * vab), 4))
        dva['quantb'] = mqb['quant']

        # vac calc
        mqc = calculo.calc_mq(self, larg, comp, va, quant * 3)
        mqq = mqc['mq']
        vac = calculo.calculova(self, mqq, va)

        if vac >= vab:
            mqc = calculo.calc_mq(self, larg, comp, va, quant * 8)
            mqc = mqc['mq']
            vac = calculo.calculova(self, mqq, va)
            if vac >= vab:
                vac = round(calculo.calculodes(self, vab, 3), 2)

        dva['vac'] = calculo.calculoaca(self, vac, inc)
        dva['resc'] = float(round((area * vac), 4))
        dva['quantc'] = mqc['quant']

        return dva

    def __str__(self):
        return self.cliente.nome + ' - ' + self.servico


class Orcamento_adesivo(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False)
    servico = models.CharField(max_length=400, blank=False, null=False)
    material = models.ForeignKey(Adesivo, on_delete=models.CASCADE, blank=False, null=False)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.CASCADE, blank=False, null=False)
    comp = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)
    larg = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)
    quantidade = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)

    def __str__(self):
        return self.cliente.nome + ' - ' + self.servico
