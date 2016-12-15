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
#View que renderiza todos os anuncios do banco de dados, independente de estarem aprovados ou não.
#
#Nome: anuncio
#Autor: Renan Basilio
#Versão: 1.0
#
#Algoritmo:
#   1. Chama o método getTodosAnuncios do módulo filters é armazena o resultado em 'anuncios'
#   2. Inicializa uma form de busca
#   3. Chama o método render com a lista de anúncios gerada e a form como parâmetros
#
####################################################################################################
def anuncio(request):
    anuncios = getTodosAnuncios()
    form = formBusca()
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form})

    
###################################################################################################
#View que renderiza anúncios do banco de dados filtrados por localidade.
#
#Nome: anuncioPorLocal
#Autor: Renan Basilio
#Versão: 1.0
#
#Algoritmo:
#   1. Chama o método getAnunciosPorLocalidade com o parâmetro localidade fornecido pela url
#   2. Inicializa uma form de busca
#   3. Chama o método render com a lista de anúncios gerada e a form como parâmetros
#
####################################################################################################
def anuncioPorLocal(request, localidade):
    anuncios = getAnunciosPorLocalidade(localidade)
    form = formBusca()
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form})
    
    
###################################################################################################
#View que renderiza anúncios do banco de dados filtrados por um termo de busca
#
#Nome: anuncioPorBusca
#Autor: Renan Basilio
#Versão: 1.0
#
#Algoritmo:
#   1. Inicializa uma form de busca
#   2. Chama o método getAnunciosPorSubstring com o parâmetro 't' fornecido pela url
#   3. Chama o método render com a lista de anúncios gerada e a form como parâmetros
#
####################################################################################################
def anuncioPorBusca(request):
    form = formBusca(request.GET)
    anuncios = getAnunciosPorSubstring(request.GET.get('t'))
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form})