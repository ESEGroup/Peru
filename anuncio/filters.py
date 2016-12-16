from .models import Anuncio
from .models import Localidade
from django.contrib.auth.models import User
from .util import escapeString

###################################################################################################
#Metodo que retorna todos os anuncios do banco de dados, independente de estarem aprovados ou nao.
#
#Nome: getTodosAnuncios
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   Preenche uma lista com todos os objetos encontrados na tabela anuncios_Anuncio
#   do Banco de Dados
#
#Utilizacao:
#   getTodosAnuncios()
#
####################################################################################################
def getTodosAnuncios():
    anuncios = Anuncio.objects.all()
    return anuncios


###################################################################################################
#Metodo que retorna anuncios do banco de dados em uma localidade e todas as demais superiores a esta
#na arvore de localidades
#
#Nome: getAnunciosPorLocalidade
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   1. Constroi uma lista de localidades a partir de buscas na tabela anuncios_Localidade recursivamente
#   2. Filtra os anuncios por seu estado de aprovacao
#   3. Filtra todos os anuncios do banco de dados pelas localidades encontradas
#
#Utilizacao:
#   getAnunciosPorLocalidade(localidade)
#       localidade e uma string correspondente ao nome_filtro de uma localidade no banco de dados
#
####################################################################################################
def getAnunciosPorLocalidade(localidade):
    currParentId = Localidade.objects.get(nome_filtro=localidade.lower())
    localidades = list()
    localidades.append(currParentId.id)
    while currParentId.parent != None:
        localidades.append(currParentId.parent.id)
        currParentId = Localidade.objects.get(id=currParentId.parent.id)
    anuncios = Anuncio.objects.all().filter(aprovado=True).filter(localidade_id__in=localidades)
    return anuncios


###################################################################################################
#Metodo que retorna anuncios do banco que contenham uma determinada string
#
#Nome: getAnunciosPorSubstring
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   1. Gera uma string segura para queries SQL via a funcao escapeString()
#   2. Gera uma string de query
#   3. Realiza uma query na tabela anuncio_anuncio utilizando a string gerada
#
#Utilizacao:
#   getAnunciosPorLocalidade(string)
#       string e a string em funcao da qual se deseja filtrar titulo e descricao
#
#Observacoes:
#   No SQLite valores booleanos sao armazenados como 0 (False) e 1 (True), portanto estes sao os
#   valores testados nas queries customizadas.
#
####################################################################################################
def getAnunciosPorSubstring(string):
    safeString = escapeString(string)
    queryString = 'SELECT * FROM anuncio_anuncio WHERE aprovado=1 AND(titulo LIKE \'%' + safeString + '%\' OR descricao LIKE \'%' + safeString + '%\')'
    anuncios = Anuncio.objects.raw(queryString)
    return anuncios
    
    
###################################################################################################
#Metodo que retorna anuncios do banco criados por um usuario especifico
#
#Nome: getAnunciosPorUsuario
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   1. Recupera da tabela de anuncios todos os anuncios e filtra pelo id do usuario fornecido
#
#Utilizacao:
#   getAnunciosPorUsuario(usuario)
#       usuario e um objeto do tipo User do django
#
####################################################################################################
def getAnunciosPorUsuario(usuario):
    anuncios = Anuncio.objects.all().filter(anunciante=usuario.id)
    return anuncios