from django import forms


###################################################################################################
#Classe que representa uma form de busca contendo um único campo t
#
#Nome: formBusca
#Autor: Renan Basilio
#Versão: 1.0
#
#Parâmetros:
#   t ("termo") é um CharField para input de texto com limite de até 100 caracteres.
####################################################################################################
class formBusca(forms.Form):
    t = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Buscar Anuncios', 'class':'form-control'}))