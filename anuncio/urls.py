from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.anuncio),
    url(r'^busca', views.anuncioPorBusca),
    url(r'^registrar/$', views.formUsuarioView.as_view(), name='registro'),
    url(r'^loc=(?P<localidade>\w+)', views.anuncioPorLocal),
    url(r'^loc=(?P<localidade>\w+)/busca', views.anuncioPorLocal),
    url(r'^reacao/$', views.reacao, name='reacao'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^aprovar/$', views.aprovar, name='aprovar'),
    url(r'^salvaredicoes', views.salvar_edicoes),
    url(r'^meus/$', views.anuncioPorUsuario),
    url(r'^pendentes/$', views.anuncioPendendoAp),
    url(r'^inserir/$', views.inserirAnuncio),
    url(r'^logout/$', views.logout_view),
     url(r'^login/$', views.login_view.as_view(), name='login'),
]
