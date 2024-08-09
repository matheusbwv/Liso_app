from django.forms import ModelForm
from .models import Receita, Despesas


class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"
        
class DespesasForm(ModelForm):
    class Meta:
        model = Despesas
        fields = "__all__"