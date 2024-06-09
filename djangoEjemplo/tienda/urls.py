from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('juego',views.juego,name='Juego'),
    path('juego/<int:comentario_pk>',views.comentarioDelete,name="comentario_delete")
]
#<!--{% url 'comentarioDelete' comentario_pk=comentario.id juego_pk=juego.id %}-->