from django.utils import timezone
from django.db import models

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

    def __str__(self):
        return self.titulo