from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Saldo)
admin.site.register(models.Despesas)
admin.site.register(models.Receita)