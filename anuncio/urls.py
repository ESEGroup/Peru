from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.anuncio),
    url(r'^local\=(?P<localidade>\w+)', views.anuncioPorLocal),
    url(r'^busca', views.anuncioPorBusca),
    url(r'^reacao/$', views.reacao, name='reacao'),
]