from django.forms import ModelForm
from .models import Orcamento_adesivo, Orcamento_filme, Orc_adesivo


class Orc_adesivoForm(ModelForm):
    class Meta:
        model = Orc_adesivo
        fields = '__all__'


class OcadesivoForm(ModelForm):
    class Meta:
        model = Orcamento_adesivo
        fields = ['data', 'cliente', 'servico', 'material', 'acabamento', 'comp', 'larg', 'quantidade']


class OcfilmeForm(ModelForm):
    class Meta:
        model = Orcamento_filme
        fields = ['data', 'cliente', 'servico', 'material', 'acabamento', 'comp', 'larg', 'quantidade']
