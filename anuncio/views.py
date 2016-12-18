from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django import forms
from django.shortcuts import render, redirect #
from django.contrib.auth import authenticate, login #
from django.views import generic #
from django.views.generic import View #
from .models import Anuncio
from .models import Localidade
from .models import Usuario #
from django.utils import timezone
from datetime import datetime
from .filters import *
from .forms import formBusca, formAnuncio, formAnuncioEdit, formUsuario #

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
    edit_forms = getFormsEdicaoDeAnuncios(anuncios)
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':"Localidade ", 'editforms':edit_forms })


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
    edit_forms = getFormsEdicaoDeAnuncios(anuncios)
    nome_local = Localidade.objects.get(nome_filtro=localidade).nome + ' '
    form = formBusca()
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':nome_local, 'editforms':edit_forms})


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
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':"Localidade ", 'editforms':edit_forms})


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
        return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':"Localidade ", 'editforms':edit_forms})
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
            return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios, 'formBusca':form, 'localidade':"Localidade ", 'editforms':edit_forms})
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

def inserirAnuncio(request):
    form_busca = formBusca()
    if request.method == 'POST':
        form = formAnuncio(request.POST)
        print "0"
        if form.is_valid():
            print "1"
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print "2"
            print form.errors
    else:
        print "3"
        form = formAnuncio()
    print "4"
    return render(request, 'anuncios/inserir.html', {'formInsert':form, 'formBusca':form_busca, 'localidade':"Localidade "})

def getFormsEdicaoDeAnuncios(listaAnuncios):
    edit_forms = list()
    for anuncio in listaAnuncios:
        edit_form = formAnuncioEdit(instance=anuncio)
        edit_forms.append(edit_form)
    return edit_forms


def salvar_edicoes(request):
    if request.method == 'POST':
        anuncio_modificado   = request.POST
        print anuncio_modificado
        anuncio             = Anuncio.objects.get(id=anuncio_modificado.get('id'))
        anuncio.titulo      = anuncio_modificado.get('titulo')
        anuncio.descricao   = anuncio_modificado.get('descricao')
        anuncio.data_inicio = anuncio_modificado.get('data_inicio_0') + " " + anuncio_modificado.get('data_inicio_1')
        anuncio.data_fim    = anuncio_modificado.get('data_fim_0') + " " + anuncio_modificado.get('data_fim_1')
        print anuncio.data_inicio
        anuncio.save()
    return HttpResponseRedirect('/')

class formUsuarioView(View):
    form_class = formUsuario
    template_name = 'anuncios/cadastro.html'
    def get(self, request):
        form_busca = formBusca()
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'formBusca':form_busca, 'localidade':"Localidade "})

    def post(self, request):
        form_busca = formBusca()
        form = self.form_class(request.POST)
        if form.is_valid():
            user      = form.save(commit=False)
            nome      = form.cleaned_data['nome']
            username  = form.cleaned_data['username']
            email     = form.cleaned_data['email']
            celular   = form.cleaned_data['celular']
            descricao = form.cleaned_data['descricao']
            password  = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('../')
        return render(request, self.template_name, {'form': form, 'formBusca':form_busca, 'localidade':"Localidade "})


