from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    #return HttpResponse("<h1>ola mundo <h1>")

    return render(request, "home.html")

def pag1_function(request):
    return render(request, "pag1.html")