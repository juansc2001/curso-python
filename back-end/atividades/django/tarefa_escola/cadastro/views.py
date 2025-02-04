from django.shortcuts import render
from .models import Aluno

def index(request):
    return render(request,'index.html')

def contatos(request):
    return render(request,"contatos.html")



def aluno_list(request):
    dados_aluno = Aluno.objects.all
    return render(request, "alunos_list.html" , {"dado": dados_aluno })