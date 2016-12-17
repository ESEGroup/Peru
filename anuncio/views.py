from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
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
#   3. Chama o metodo render
#
####################################################################################################
def anuncio(request):
    anuncios = getTodosAnunciosValidos()
    form = formBusca()
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':"Localidade "})


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
#   3. Chama o metodo render
#
####################################################################################################
def anuncioPorLocal(request, localidade):
    anuncios = getAnunciosPorLocalidade(localidade)
    nome_local = Localidade.objects.get(nome_filtro=localidade).nome + ' '
    form = formBusca()
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':nome_local})


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
#   3. Chama o metodo render
#
####################################################################################################
def anuncioPorBusca(request):
    form = formBusca(request.GET)
    anuncios = getAnunciosPorSubstring(request.GET.get('t'))
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':"Localidade "})
    

###################################################################################################
#View que renderiza anuncios do banco de dados filtrados pelo usuario que os criou
#
#Nome: anuncioPorUsuario
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   1. Verifica se o usuario esta autenticado
#   2. Se nao retorna uma HttpResponseForbidden
#   3. Se sim, inicializa form de busca e constroi lista de anuncios a partir do metodo getAnunciosPorUsuario
#   4. Chama o metodo render
#
####################################################################################################
def anuncioPorUsuario(request):
    if request.user.is_authenticated():
        form = formBusca()
        anuncios = getAnunciosPorUsuario(request.user)
        return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':"Localidade "})
    else:
        return HttpResponseForbidden()
        
        
###################################################################################################
#View que renderiza anuncios do banco de dados com aprovacao pendente
#
#Nome: anuncioPendendoAp
#Autor: Renan Basilio
#Versao: 0.1
#
#Algoritmo:
#   1. Verifica se o usuario esta autenticado, se nao retorna uma HttpResponseForbidden
#   2. Se sim verifica se o usuario tem permissao para aprovar anuncios, se nao tiver passa o controle
#      para a view geral
#   3. Se sim:
#       Inicializa form de busca
#       Recupera os anuncios com aprovacao pendente pelo metodo getAnunciosApPendente
#       Chama o metodo render
#
####################################################################################################
def anuncioPendendoAp(request):
    if request.user.is_authenticated():
        if True:    ## Verificar se o usuario possui permissao para aprovar anuncios
            form=formBusca()
            anuncios = getAnunciosApPendente()
            return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':"Localidade "})
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()
        
        
def reacao(request):
    anuncioId = None
    if request.method == 'GET':
        anuncioId = request.GET.get('id')
        reacaoType = request.GET.get('reacao')
    reacao = 0
    if anuncioId:
        anuncio = Anuncio.objects.get(id=int(anuncioId))
        if anuncio:
            reacao = anuncio.incrementarReacao(reacaoType)

    return HttpResponse(reacao)

def delete(request):
    anuncioId = None
    if request.method == 'GET':
        anuncioId = request.GET.get('id')
    if anuncioId:
        anuncio = Anuncio.objects.get(id=int(anuncioId))
        anuncio.delete()
    return HttpResponse()

def aprovar(request):
    anuncioId = None
    if request.method == 'GET':
        anuncioId = request.GET.get('id')
    if anuncioId:
        anuncio = Anuncio.objects.get(id=int(anuncioId))
        anuncio.aprovado = True
        anuncio.ap_pendente = False
        anuncio.save()
    return HttpResponse()