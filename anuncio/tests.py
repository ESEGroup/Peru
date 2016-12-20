import datetime

from django.test import TestCase
from django.utils import timezone
from django.db import models
from django.urls import reverse

from .models import Anuncio, Localidade, Usuario

class TestesUnitariosAnuncio(TestCase):

	####################################################
	#Cenário 1:
	#
	#Título: Choppada Engenharia Eletrônica (válido)
	#Data Inicio: data atual (válido)
	#Data fim: data atual + 10 dias (válido)
	####################################################
	def teste_cenario_1(self):
		inicio = timezone.now()
		fim = inicio + datetime.timedelta(days=10)
		c_user = Usuario(nome="Test User")
		c_user.save()
		c_local = Localidade(nome="Web")
		c_local.save()
		anunciante = Usuario.objects.get(nome="Test User")
		localidade = Localidade.objects.get(nome = "Web")
		anuncio = Anuncio(anunciante=anunciante, titulo="Choppada Engenharia Eletrônica", descricao="", data_inicio=inicio, data_fim=fim, localidade=localidade)
		self.assertIs(anuncio.publicar(), None)

	####################################################
	#Cenário 2:
	#
	#Título: Choppada de  Engenharia Eletrônica, de Engenharia de Controle e Automação, de Engenharia de  Computação e Informação, de Engenharia de Produção, de Engenharia Metalúrgica, de Psicologia e de Ciências Sociais (inválido)
	#Data Inicio: data atual (válido)
	#Data fim: data atual + 10 dias (válido)
	####################################################
	def teste_cenario_2(self):
		c_user = Usuario(nome="Test User")
		c_user.save()
		c_local = Localidade(nome="Web")
		c_local.save()

		anunciante = Usuario.objects.get(nome="Test User")
		localidade = Localidade.objects.get(nome = "Web")
		inicio = timezone.now()
		fim = inicio + datetime.timedelta(days=10)
		titulo = "Choppada de  Engenharia Eletrônica, de Engenharia de Controle e Automação, de Engenharia de  Computação e Informação, de Engenharia de Produção, de Engenharia Metalúrgica, de Psicologia e de Ciências Sociais"
		anuncio = Anuncio(anunciante=anunciante, titulo=titulo, data_inicio=inicio, data_fim=fim, localidade=localidade)
		self.assertIsNot(anuncio.publicar(), None)

	####################################################
	#Cenário 3:
	#
	#Título: Choppada Engenharia Eletrônica (válido)
	#Data Inicio: em branco (inválido)
	#Data fim: data atual + 10 dias (válido)
	####################################################
	def teste_cenario_3(self):
		c_user = Usuario(nome="Test User")
		c_user.save()
		c_local = Localidade(nome="Web")
		c_local.save()

		anunciante = Usuario.objects.get(nome="Test User")
		localidade = Localidade.objects.get(nome = "Web")
		fim = timezone.now() + datetime.timedelta(days=10)
		titulo = "Choppada de  Engenharia Eletrônica, de Engenharia de Controle e Automação, de Engenharia de  Computação e Informação, de Engenharia de Produção, de Engenharia Metalúrgica, de Psicologia e de Ciências Sociais"
		anuncio = Anuncio(anunciante=anunciante, titulo=titulo, data_fim=fim, localidade=localidade)
		self.assertIsNot(anuncio.publicar(), None)

	####################################################
	#Cenário 4:
	#
	#Título: Choppada Engenharia Eletrônica (válido)
	#Data Inicio: em branco (inválido)
	#Data fim: data atual + 10 dias (válido)
	####################################################
	def teste_cenario_4(self):
		c_user = Usuario(nome="Test User")
		c_user.save()
		c_local = Localidade(nome="Web")
		c_local.save()

		anunciante = Usuario.objects.get(nome="Test User")
		localidade = Localidade.objects.get(nome = "Web")
		inicio = timezone.now()
		titulo = "Choppada de  Engenharia Eletrônica, de Engenharia de Controle e Automação, de Engenharia de  Computação e Informação, de Engenharia de Produção, de Engenharia Metalúrgica, de Psicologia e de Ciências Sociais"
		anuncio = Anuncio(anunciante=anunciante, titulo=titulo, data_inicio=inicio, localidade=localidade)
		self.assertIsNot(anuncio.publicar(), None)





