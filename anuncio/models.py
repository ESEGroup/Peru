from django.utils import timezone
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User #

class Anuncio(models.Model):
    id           = models.AutoField(primary_key=True)
    anunciante   = models.ForeignKey('auth.User')
    titulo       = models.CharField(max_length=200)
    descricao    = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_inicio  = models.DateTimeField()
    data_fim     = models.DateTimeField()
    localidade   = models.ForeignKey('Localidade')
    aprovado     = models.BooleanField(default=False)
    ap_pendente  = models.BooleanField(default=True)
    curtir       = models.PositiveIntegerField(default=0)
    amar         = models.PositiveIntegerField(default=0)
    odiar        = models.PositiveIntegerField(default=0)

    def publicar(self):
        self.data_criacao = timezone.now()
        self.save()

    def progresso(self):
        tempo_passado   = (timezone.now() - self.data_inicio).total_seconds()
        intervalo_total = self.intervalo()

        if tempo_passado <= 0:
            return 0
        elif tempo_passado >= intervalo_total:
            return 100
        else:
            return (tempo_passado*100) / (intervalo_total)

    def intervalo(self):
        return (self.data_fim - self.data_inicio).total_seconds()

    def getInicio(self):
        return self.getDataString(self.data_inicio)

    def getFim(self):
        return self.getDataString(self.data_fim)

    def getCriacao(self):
        return self.getDataString(self.data_criacao)

    def getDataString(self, dt):
        return dt.strftime('%d/%m/%Y %H:%M')

    def incrementarReacao(self, type):
        reacao = 0
        if type == "amar":
            reacao = self.amar = self.amar + 1
        elif type == "curtir":
            reacao = self.curtir = self.curtir + 1
        elif type == "odiar":
            reacao = self.odiar = self.odiar + 1
        else:
            print("Deu merda");
        self.save()
        return reacao

    def __unicode__(self):
        return self.titulo

class Localidade(models.Model):
    id          = models.AutoField(primary_key=True)
    nome        = models.CharField(max_length=50)
    nome_filtro = models.CharField(max_length=10)
    parent      = models.ForeignKey('Localidade', blank=True, null=True)

    def __unicode__(self):
        return self.nome

class Usuario(User):
    nome = models.CharField(max_length=256)
    celular = models.CharField(max_length=256)
    descricao = models.CharField(max_length=256)
    def __str__(self):
        return self.nome