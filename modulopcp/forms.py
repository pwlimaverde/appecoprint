from django.forms import ModelForm
from .models import Reg_entregav2


class Reg_entregaForm(ModelForm):
    class Meta:
        model = Reg_entregav2
        fields = '__all__'
