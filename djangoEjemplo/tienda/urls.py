from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('juego',views.juego,name='juego'),
    path('comentario_delete/<int:comentario_pk>',views.comentarioDelete,name="comentario_delete"),
    path('comentario_edit/<int:comentario_pk>',views.comentario,name="comentario"),
    path('comentario_edit/comentario_update',views.comentarioUpdate,name="comentario_update"),
]
#<!--{% url 'comentarioDelete' comentario_pk=comentario.id juego_pk=juego.id %}-->