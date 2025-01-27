from django.shortcuts import render


def base(request):
    return render(request,'base.html')

def pag_inicial(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def servicos(request):
    return render(request,'servicos.html')

