from django.shortcuts import render
from .models import Anuncio
from django.utils import timezone
from datetime import datetime

# Create your views here.
def anuncio(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios})
