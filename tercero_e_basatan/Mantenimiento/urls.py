from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicioDef, name='inicio'),
    path('crearJuguete/', views.crearJugueteDef, name='crear'),
    path('registrarJuguete/', views.registrarJugueteDef, name='registrarJuguete'),
    path('editarJuguete/<int:id>', views.editarJugueteDef, name='editarJuguete'),
    path('edicionJuguete/', views.edicionJugueteDef, name='edicionJuguete'),
    path('borrarJuguete/<id>', views.borraJugueteDef, name='borrarJuguete'),
    path('buscar_juguete/', views.buscar_juguetes, name='buscarjuguete'),

]