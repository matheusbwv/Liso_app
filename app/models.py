from django.db import models

class saldo(models.Model):
  valor = models.FloatField()

class despesa(models.Model):
  descricao = models.CharField(max_length=120)
  valor = models.FloatField()
  categoria = models.SmallIntegerField()
class receita(models.Model):
  descricao = models.CharField(max_length=120)
  valor = models.FloatField()
  categoria = models.SmallIntegerField()
  
