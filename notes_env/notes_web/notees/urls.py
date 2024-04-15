from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # URL para la vista de inicio
    path('inicio/', views.pagina_inicio, name='pagina_inicio'),  # URL para la página de inicio deseada
    path('login/', views.inicio_sesion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('lista_notas/', views.lista_notas, name='lista_notas'),
    path('crear/', views.crear_nota, name='creanota'),  # Nueva URL para crear una nota
    path('borrar/<int:nota_id>/', views.borrar_nota, name='borrar_nota'),  # Nueva URL para borrar una nota
    path('nota/<int:nota_id>/', views.detalle_nota, name='detalle_nota'),
]

'''
path('lo que aparece en la url al buscar', a lo que redirigimos (métodos), ...)
'''