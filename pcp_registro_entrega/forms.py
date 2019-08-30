from django.forms import ModelForm
from .models import RegistroEntrega


class RegistroEntregaForm(ModelForm):
    class Meta:
        model = RegistroEntrega
        fields = '__all__'
