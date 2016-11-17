from django.utils import timezone
from django.db import models
from datetime import datetime

# Create your models here.
class Anuncio(models.Model):
    id           = models.AutoField(primary_key=True)
    anunciante   = models.ForeignKey('auth.User')
    titulo       = models.CharField(max_length=200)
    descricao    = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_inicio  = models.DateTimeField()
    data_fim     = models.DateTimeField()
    localidade   = models.CharField(max_length=50)

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

    def get_dt_inicio(self):
        return self.get_dt_string(self.data_inicio)

    def get_dt_fim(self):
        return self.get_dt_string(self.data_fim)

    def get_dt_criacao(self):
        return self.get_dt_string(self.data_criacao)

    def get_dt_string(self, dt):
        return dt.strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return self.titulo