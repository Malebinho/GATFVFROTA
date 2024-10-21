from django.shortcuts import render

# Create your views here.

def cadastro_func(request):
    return render(request, 'cadastro_func.html')


def login(request):
    return render(request, 'login.html')

