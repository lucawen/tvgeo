from django.conf.urls import url
from django.contrib import admin

from clima import views
from djgeojson.views import GeoJSONLayerView


urlpatterns = [
    url(r'^$', views.normais ),
    url(r'^accounts/login/$', views.loginusr ),
    url(r'^sair/$', views.sair ),
    url(r'^normais/$', views.normais ),
    url(r'^automaticas/$', views.automaticas ),
    url(r'^grafnormais/(?P<station>\d+)/(?P<texto>[\w ]+)/$', views.grafnormais ),
    url(r'^grafautomatica/(?P<station>\d+)/(?P<mes>\d+)/(?P<ano>\d+)/(?P<texto>[\w ]+)/$', views.grafAutomatica ),
    url(r'^getautomaticajson/(?P<station>\d+)/$', views.getautomaticajson),
    url(r'^grafautomaticatotal/(?P<station>\d+)/(?P<texto>[\w ]+)/$', views.grafAutomaticaTotal),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model= views.Station, properties=('id', 'Altitude', 'Codigo', 'Nome','Estado',"tipo",'tipo',)), name='data'),
    url(r'^fire.geojson$', GeoJSONLayerView.as_view(model= views.FocoItem), name='data'),
    url(r'^mapaestacoes/$', views.mapaestacoes),
    url(r'^mapafocoincendio/$', views.mapafocoincendio),
    url(r'^focoCalor/(?P<id>\d+)/$', views.focoCalor),
]