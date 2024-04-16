from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.pagina_inicio, name='pagina_inicio'),
    path('login/', views.inicio_sesion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('lista_notas/', views.lista_notas, name='lista_notas'),
    path('crear/', views.crear_nota, name='creanota'),
    path('editar/<int:nota_id>/', views.editar_nota, name='editar_nota'),
    path('borrar/<int:nota_id>/', views.borrar_nota, name='borrar_nota'),
    path('nota/<int:nota_id>/', views.detalle_nota, name='detalle_nota'),
]

'''
path('lo que aparece en la url al buscar', a lo que redirigimos (métodos), ...)
'''