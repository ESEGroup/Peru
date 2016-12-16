from django import forms


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