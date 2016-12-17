from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.anuncio),
    url(r'^busca', views.anuncioPorBusca),
    url(r'^loc=(?P<localidade>\w+)', views.anuncioPorLocal),
    url(r'^loc=(?P<localidade>\w+)/busca', views.anuncioPorLocal),
    url(r'^reacao/$', views.reacao, name='reacao'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^aprovar/$', views.aprovar, name='aprovar'),
    url(r'^meus/$', views.anuncioPorUsuario),
    url(r'^pendentes/$', views.anuncioPendendoAp),
    url(r'^inserir/$', views.inserirAnuncio)
]
