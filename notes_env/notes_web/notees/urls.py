from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.lista_notas, name='lista_notas'),
    #path('crear', views.crear_nota, name='creanota'),
]
