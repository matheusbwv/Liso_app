from django.urls import path
from .views import verSaldo, adicionarReceita,adicionarDespesa, verDespesas, verReceitas

urlpatterns = [
    path('', verSaldo),
    path('addR/', adicionarReceita ),
    path('addD/', adicionarDespesa ),
    path('verD/', verDespesas ),
    path('verR/', verReceitas ),
]