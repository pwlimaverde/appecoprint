from django.forms import ModelForm
from .models import Orcamento_adesivo, Orcamento_filme


class OcadesivoForm(ModelForm):
    class Meta:
        model = Orcamento_adesivo
        fields = '__all__'


class OcfilmeForm(ModelForm):
    class Meta:
        model = Orcamento_filme
        fields = '__all__'
