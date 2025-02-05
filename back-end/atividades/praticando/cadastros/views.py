from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'home.html')

def loja(request):

    return render(request, 'loja.html')