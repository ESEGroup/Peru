from django import forms
from .models import Anuncio, Localidade
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.admin import widgets
import datetime


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

class formAnuncio(forms.ModelForm):
    anunciante   = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'insert-form form-control'}))
    titulo       = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'insert-form form-control'}))
    descricao    = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={'rows': 10, 'class': 'insert-form form-control'}))
    data_inicio  = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime(attrs={'class': 'insert-form form-control datetimepicker'}))
    data_fim     = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime(attrs={'class': 'insert-form form-control datetimepicker'}))
    localidade   = forms.ModelChoiceField(queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class': 'insert-form form-control'}))
    aprovado     = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)
    ap_pendente  = forms.BooleanField(widget=forms.HiddenInput(), initial=True, required=False)
    data_criacao = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now, required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Anuncio
        exclude = ['odiar', 'amar', 'curtir']

    def __init__(self, *args, **kwargs):
        super(formAnuncio, self).__init__(*args, **kwargs)
        self.fields['data_inicio'].widget = widgets.AdminSplitDateTime()
        self.fields['data_fim'].widget = widgets.AdminSplitDateTime()
