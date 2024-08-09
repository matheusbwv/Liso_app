from rest_framework import serializers

from .models import Saldo, Despesas, Receita

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saldo
        fields = ["valor"]
        
class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = ["descricao","valor","categoria"]
        

class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ["descricao","valor","categoria"]