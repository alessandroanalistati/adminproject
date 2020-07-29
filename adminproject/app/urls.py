
from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import inserir_sala, listar_sala, listar_sala_id, editar_sala, remover_sala

app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_salas', listar_sala, name='listar_salas'),
    path('cadastrar_sala', inserir_sala, name='cadastrar_sala'),
    path('listar/<int:id>', listar_sala_id, name='listar_sala_id'),
    path('editar/<int:id>', editar_sala, name='editar_sala'),
    path('remover/<int:id>', remover_sala, name='remover_sala')
]

