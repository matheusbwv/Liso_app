from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Saldo, Despesas, Receita
from .serializers import SaldoSerializer, ReceitasSerializer, DespesasSerializer
from .forms import DespesasForm, ReceitaForm

# Create your views here.

def alterarSaldo(valor, tipo):
    if tipo == 1:
        saldo = Saldo.objects.get(id = 1)
        saldo.valor += valor
        saldo.save()
    else:
        saldo = Saldo.objects.get(id = 1)
        saldo.valor -= valor
        saldo.save()
        
@api_view(["GET"])
def verSaldo(request):
    saldo = Saldo.objects.all()
    serializer = SaldoSerializer(saldo,many = True)
    dados = {
        "mensagem" : "Esse é seu saldo:",
        "saldo" : serializer.data
    }
    return Response(dados)

@api_view(["POST"])
def adicionarReceita(request):
        form = ReceitaForm(request.data)
        if form.is_valid():
            alterarSaldo(request.data['valor'], 1)
            form.save()
            return Response({
                "message": "receita adicionada com sucesso!"
            })
        elif not form.is_valid():
            return Response({
                    "message": "formulario invalido!"
                })
        
        return Response({
                "request" : request.data,
                "message": "Ocorreu um erro!",
            })
        
@api_view(["POST"])
def adicionarDespesa(request):
    try:
        form = DespesasForm(request.data)
        if form.is_valid():
            alterarSaldo(request.data['valor'], 2)
            form.save()
            return Response({
                "message": "Despesa adicionada com sucesso!"
            })
    except:
        return Response({
            "message": "Ocorreu um erro!"
        })
        
@api_view(["GET"])
def verDespesas(request):
    despesas = Despesas.objects.all()
    serializer = DespesasSerializer(despesas,many = True)
    dados = {
        "mensagem" : "Esse é seu saldo:",
        "despesas" : serializer.data
    }
    return Response(dados)
    
@api_view(["GET"])
def verReceitas(request):
    receita = Receita.objects.all()
    serializer = ReceitasSerializer(receita,many = True)
    dados = {
        "mensagem" : "Esse é seu saldo:",
        "receitas" : serializer.data
    }
    return Response(dados)