from django.forms import ModelForm
from .models import Reg_entrega


class Reg_entregaForm(ModelForm):
    class Meta:
        model = Reg_entrega
        fields = '__all__'
