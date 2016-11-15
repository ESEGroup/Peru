from django.shortcuts import render
from .models import Anuncio
from django.utils import timezone
from datetime import datetime

# Create your views here.
def anuncio(request):
    anuncios = Anuncio.objects.all()
    for anuncio in anuncios:
        anuncio.data_inicio = anuncio.data_inicio.strftime('%d/%m/%Y %H:%M')
        anuncio.data_fim = anuncio.data_fim.strftime('%d/%m/%Y %H:%M')
        anuncio.data_criacao = anuncio.data_criacao.strftime('%d/%m/%Y %H:%M')
        print anuncio
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios})
