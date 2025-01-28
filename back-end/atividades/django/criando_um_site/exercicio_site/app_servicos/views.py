from django.shortcuts import render

def pag_inicial(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def servicos(request):
    return render(request,'servicos.html')

def contatos(request):
    return render(request,'contatos.html')

def home(request):
    return render(request,'home.html')