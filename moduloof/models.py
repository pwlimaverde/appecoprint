from tkinter import CASCADE

from django.db import models


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
        a = float(6)
        b = float(5)
        c = float(4)
        d = float(3)
        e = float(2)
        f = float(1)
        g = float(0)
        ma = float(70)
        mb = float(95)
        mc = float(120)
        md = float(150)
        me = float(250)
        mf = float(300)
        mg = float(350)

        # Calculos Valores do metro
        if mqg >= mg:
            return float(vg + g)
        if mqg >= mf:
            return float(vg + f)
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


# classes Models
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

    def calc_vf(self):
        # Constantes
        mi = float(6)
        vatmi = int(700)
        conv = int(1000)

        # Dados BD
        larg = float(self.larg)
        comp = float(self.comp)
        rend = float(self.material.rendimento)
        gram = float(self.material.gramatura)
        va = float(self.material.valor_de_venda)
        inc = self.acabamento.incremento
        quant = int(self.quantidade)

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

class Adesivo(models.Model):
    descricao = models.CharField(max_length=200, blank=False, null=False)
    tipo = models.ForeignKey(Tpadesivo, on_delete=CASCADE, blank=False, null=False)
    valor_de_venda = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao


class Orcamento_adesivo(models.Model, calculo):
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

    def calc_va(self):
        cva = {}
        # varbd
        comp = self.comp
        larg = self.larg
        inc = float(self.acabamento.incremento)
        va = float(self.material.valor_de_venda)
        quant = int(self.quantidade)

        area = calculo.calcarea(
            self,
            comp,
            larg
        )

        # vaa calc
        mqa = calculo.calc_mq(
            self,
            larg,
            comp,
            va,
            quant
        )


        bcva = calculo.calculova(
            self,
            mqa['mq'],
            va
        )

        cva['vaa'] = calculo.calculoaca(
            self,
            bcva,
            inc
        )

        cva['mqa'] = mqa['mq']
        cva['resa'] = float(round((area * cva['vaa']), 4))
        cva['quanta'] = mqa['quant']
        cva['quantmi'] = int(mqa['quantmi'])

        if cva['quanta'] <= cva['quantmi']:
            quant = cva['quantmi']

        # vami calc
        mqmi = calculo.calc_mq(
            self,
            larg,
            comp,
            va,
            cva['quantmi']
        )

        bcvami = calculo.calculova(
            self,
            mqmi['mq'],
            va
        )
        cva['vami'] = calculo.calculoaca(
            self,
            bcvami,
            inc
        )

        cva['mqmi'] = mqmi['mq']
        cva['resmi'] = float(round((area * cva['vami']), 4))

        # vab calc
        mqb = calculo.calc_mq(
            self,
            larg,
            comp,
            va,
            quant * 2
        )

        vab = calculo.calculova(
            self,
            mqb['mq'],
            va
        )

        if vab >= cva['vaa']:
            mqb = calculo.calc_mq(
                self,
                larg,
                comp,
                va,
                quant * 4
            )

            vab = calculo.calculova(
                self,
                mqb['mq'],
                va
            )

            if vab >= cva['vaa']:
                vab = round(calculo.calculodes(cva['vaa'], 3), 2)

        bcvb = calculo.calculova(
            self,
            mqb['mq'],
            va
        )

        cva['vab'] = calculo.calculoaca(
            self,
            bcvb,
            inc
        )

        cva['mqb'] = mqb['mq']
        cva['resb'] = float(round((area * vab), 4))
        cva['quantb'] = mqb['quant']

        # vac calc
        mqc = calculo.calc_mq(
            self,
            larg,
            comp,
            va,
            quant * 3
        )

        vac = calculo.calculova(
            self,
            mqc['mq'],
            va
        )

        if vac >= cva['vab']:
            mqc = calculo.calc_mq(
                self,
                larg,
                comp,
                va,
                quant * 8
            )

            cva['vac'] = calculo.calculova(
                self,
                mqc['mq'],
                va
            )

            if vac >= cva['vab']:
                vac = round(calculo.calculodes(self, cva['vab'], 3), 2)

        bcvc = calculo.calculova(
            self,
            mqc['mq'],
            va
        )

        cva['vac'] = calculo.calculoaca(
            self,
            bcvc,
            inc
        )

        cva['mqc'] = mqc['mq']
        cva['resc'] = float(round((area * vac), 4))
        cva['quantc'] = mqc['quant']

        return cva

    def vami(self):
        valor = self.calc_va()
        return valor['vami']

    def mqmi(self):
        valor = self.calc_va()
        return valor['mqmi']

    def resmi(self):
        valor = self.calc_va()
        return valor['resmi']

    def total_mi(self):
        valor = self.calc_va()
        resmi = valor['resmi']
        quantmi = valor['quantmi']
        return round(resmi * quantmi, 4)

    def quantmi(self):
        valor = self.calc_va()
        return valor['quantmi']

    def vaa(self):
        valor = self.calc_va()
        vaa = float(valor['vaa'])
        vmi = float(valor['vami'])
        if vaa >= vmi:
            va = valor['vami']
            return va
        else:
            va = valor['vaa']
            return va

    def mqa(self):
        valor = self.calc_va()
        return valor['mqa']

    def resa(self):
        valor = self.calc_va()
        return valor['resa']

    def total_a(self):
        valor = self.calc_va()
        resa = valor['resa']
        quanta = valor['quanta']
        return round(resa * quanta, 4)

    def quanta(self):
        valor = self.calc_va()
        return int(valor['quanta'])

    def vab(self):
        valor = self.calc_va()
        return valor['vab']

    def mqb(self):
        valor = self.calc_va()
        return valor['mqb']

    def resb(self):
        valor = self.calc_va()
        return valor['resb']

    def total_b(self):
        valor = self.calc_va()
        resb = valor['resb']
        quantb = valor['quantb']
        return round(resb * quantb, 4)

    def quantb(self):
        valor = self.calc_va()
        return int(valor['quantb'])

    def vac(self):
        valor = self.calc_va()
        return valor['vac']

    def mqc(self):
        valor = self.calc_va()
        return valor['mqc']

    def resc(self):
        valor = self.calc_va()
        return valor['resc']

    def total_c(self):
        valor = self.calc_va()
        resc = valor['resc']
        quantc = valor['quantc']
        return round(resc * quantc, 4)

    def quantc(self):
        valor = self.calc_va()
        return int(valor['quantc'])

