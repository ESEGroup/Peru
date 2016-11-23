from django.shortcuts import render
from .models import Anuncio
from .models import Localidade
from django.utils import timezone
from datetime import datetime

# Create your views here.    
def anuncio(request, localidade = None):
    if localidade == None:
        anuncios = Anuncio.objects.all()
    else:
        currParentId = Localidade.objects.get(nome_filtro=localidade)
        localidades = list()
        localidades.append(currParentId.id)
        while currParentId.parent != None:
            localidades.append(currParentId.parent.id)
            currParentId = Localidade.objects.get(id=currParentId.parent.id)
        anuncios = Anuncio.objects.all().filter(localidade_id__in=localidades).filter(aprovado=True)
    return render(request, 'anuncios/anuncios.html', {'anuncios': anuncios})
