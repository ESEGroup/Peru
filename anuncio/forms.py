from django import forms
from .models import Anuncio, Localidade, Usuario #
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
    t = forms.CharField(max_length = 100, label='', widget=forms.TextInput(attrs={'placeholder': 'Buscar Anuncios', 'class':'form-control'}))


###################################################################################################
#Classe que representa uma form de edicao de anuncios
#
#Nome: formBusca
#Autores: Igor Abreu, Renan Basilio
#Versao: 0.1
#
#Parametros:
####################################################################################################
class formAnuncio(forms.ModelForm):
    id           = forms.IntegerField(widget=forms.HiddenInput())
    anunciante   = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all())
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
        exclude = ['anunciante', 'odiar', 'amar', 'curtir', 'aprovado', 'ap_pendente', 'data_criacao']

    def __init__(self, *args, **kwargs):
        super(formAnuncio, self).__init__(*args, **kwargs)
        self.fields['data_inicio'].widget = widgets.AdminSplitDateTime()
        self.fields['data_fim'].widget = widgets.AdminSplitDateTime()
        if kwargs.get('instance'):
            id = kwargs.get('instance').id

class formUsuario(forms.ModelForm):
    password  = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'insert-form form-control'}))
    nome      = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'insert-form form-control'}))
    username  = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'insert-form form-control'}))
    email     = forms.CharField(max_length=256, widget=forms.EmailInput(attrs={'class': 'insert-form form-control'}))
    descricao = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={'rows': 10, 'class': 'insert-form form-control'}))
    celular   = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'insert-form form-control'}))

    class Meta:
        model = Usuario
        fields = ['nome', 'username', 'email', 'descricao', 'celular', 'password']
