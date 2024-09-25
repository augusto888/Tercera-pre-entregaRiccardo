from django.urls import path
from .views import index, crear_cliente, crear_entrenador, crear_clase, listar_clases

urlpatterns = [
    path('', index, name='index'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_entrenador/', crear_entrenador, name='crear_entrenador'),
    path('crear_clase/', crear_clase, name='crear_clase'),
    path('listar_clases/', listar_clases, name='listar_clases'),
]
