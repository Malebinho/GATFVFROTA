from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def cadastro_func(request):
    return render(request, 'cadastro_func.html')

@login_required
def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'index.html')

