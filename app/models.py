from django.db import models

# Create your models here.

class Saldo(models.Model):
    valor = models.FloatField()
    
    
class Despesas(models.Model):
    descricao = models.CharField(max_length=120)
    valor =  models.FloatField()
    categoria = models.SmallIntegerField()
     
class Receita(models.Model):
    descricao = models.CharField(max_length=120)
    valor =  models.FloatField()
    categoria = models.SmallIntegerField()
    