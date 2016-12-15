from .models import Anuncio
from .models import Localidade
from .util import escapeString

###################################################################################################
#Método que retorna todos os anuncios do banco de dados, independente de estarem aprovados ou não.
#
#Nome: getTodosAnuncios
#Autor: Renan Basilio
#Versão: 1.0
#
#Algoritmo:
#   Preenche uma lista com todos os objetos encontrados na tabela anuncios_Anuncio 
#   do Banco de Dados
#
#Utilização:
#   getTodosAnuncios()
####################################################################################################
def getTodosAnuncios():
    anuncios = Anuncio.objects.all()
    return anuncios

    
###################################################################################################
#Método que retorna anuncios do banco de dados em uma localidade e todas as demais superiores a esta
#na árvore de localidades
#
#Nome: getAnunciosPorLocalidade
#Autor: Renan Basilio
#Versão: 1.0
#
#Algoritmo:
#   1. Constroi uma lista de localidades a partir de buscas na tabela anuncios_Localidade recursivamente
#   2. Filtra os anuncios por seu estado de aprovação
#   3. Filtra todos os anuncios do banco de dados pelas localidades encontradas
#
#Utilização:
#   getAnunciosPorLocalidade(localidade)
#       localidade é uma string correspondente ao nome_filtro de uma localidade no banco de dados
####################################################################################################
def getAnunciosPorLocalidade(localidade):
    currParentId = Localidade.objects.get(nome_filtro=localidade)
    localidades = list()
    localidades.append(currParentId.id)
    while currParentId.parent != None:
        localidades.append(currParentId.parent.id)
        currParentId = Localidade.objects.get(id=currParentId.parent.id)
    anuncios = Anuncio.objects.all().filter(aprovado=True).filter(localidade_id__in=localidades)
    return anuncios

    
###################################################################################################
#Método que retorna anúncios do banco que contenham uma determinada string
#
#Nome: getAnunciosPorSubstring
#Autor: Renan Basilio
#Versão: 1.0
#
#Algoritmo:
#   1. Gera uma string segura para queries SQL via a função escapeString()
#   2. Gera uma string de query
#   3. Realiza uma query na tabela anuncio_anuncio utilizando a string gerada
#
#Utilização:
#   getAnunciosPorLocalidade(string)
#       string é a string em função da qual se deseja filtrar título e descrição
#
#Observações:
#   No SQLite valores booleanos são armazenados como 0 (False) e 1 (True), portanto estes são os
#   valores testados nas queries customizadas.
####################################################################################################
def getAnunciosPorSubstring(string):
    safeString = escapeString(string)
    queryString = 'SELECT * FROM anuncio_anuncio WHERE aprovado=1 AND(titulo LIKE \'%' + safeString + '%\' OR descricao LIKE \'%' + safeString + '%\')'
    anuncios = Anuncio.objects.raw(queryString)
    return anuncios