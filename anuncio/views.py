from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import Anuncio
from .models import Localidade
from django.utils import timezone
from datetime import datetime
from .filters import *
from .forms import formBusca

# Create your views here.

###################################################################################################
#View que renderiza todos os anuncios do banco de dados, independente de estarem aprovados ou nao.
#
#Nome: anuncio
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   1. Chama o metodo getTodosAnuncios do modulo filters e armazena o resultado em 'anuncios'
#   2. Inicializa uma form de busca
#   3. Chama o metodo render com a lista de anuncios gerada e a form como parametros
#
####################################################################################################
def anuncio(request):
    anuncios = getTodosAnuncios()
    form = formBusca()
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form})


###################################################################################################
#View que renderiza anuncios do banco de dados filtrados por localidade.
#
#Nome: anuncioPorLocal
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   1. Chama o metodo getAnunciosPorLocalidade com o parametro localidade fornecido pela url
#   2. Inicializa uma form de busca
#   3. Chama o metodo render com a lista de anuncios gerada e a form como parametros
#
####################################################################################################
def anuncioPorLocal(request, localidade):
    anuncios = getAnunciosPorLocalidade(localidade)
    form = formBusca()
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form})


###################################################################################################
#View que renderiza anuncios do banco de dados filtrados por um termo de busca
#
#Nome: anuncioPorBusca
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   1. Inicializa uma form de busca
#   2. Chama o metodo getAnunciosPorSubstring com o parametro 't' fornecido pela url
#   3. Chama o metodo render com a lista de anuncios gerada e a form como parametros
#
####################################################################################################
def anuncioPorBusca(request):
    form = formBusca(request.GET)
    anuncios = getAnunciosPorSubstring(request.GET.get('t'))
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form})