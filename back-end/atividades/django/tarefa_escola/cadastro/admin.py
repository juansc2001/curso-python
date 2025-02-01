from django.contrib import admin
from .models import Aluno
# Register your models here.

#Esta configuração permite acessar nosso banco de dados dentro do painel administrativo 
admin.site.register(Aluno)