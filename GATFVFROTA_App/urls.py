from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_func/' , views.cadastro_func, name='cadastro_func'),
    ##path('login/' , views.login, name='login'),
    path('home/' , views.home, name='home'),
]
