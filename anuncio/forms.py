from django import forms
from .models import Anuncio, Localidade
from django.utils import timezone
from django.contrib.auth.models import User

###################################################################################################
#Classe que representa uma form de busca contendo um unico campo t
#
#Nome: formBusca
#Autor: Renan Basilio
#Versao: 1.0
#
#Parametros:
#   t ("termo") e um CharField para input de texto com limite de ate 100 caracteres.
####################################################################################################
class formBusca(forms.Form):
    t = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Buscar Anuncios', 'class':'form-control'}))

class formAnuncio(forms.Form):
    anunciante   = forms.ModelChoiceField(queryset=User.objects.all())
    titulo       = forms.CharField(max_length=200)
    descricao    = forms.CharField(max_length=4000)
    data_criacao = timezone.now
    data_inicio  = forms.DateTimeField()
    data_fim     = forms.DateTimeField()
    localidade   = forms.ModelChoiceField(queryset=Localidade.objects.all())

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Anuncio
        exclude = ('anunciante', 'data_criacao')
