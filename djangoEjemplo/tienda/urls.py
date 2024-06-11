from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('juego',views.juego,name='juego'),
    path('comentario_delete/<int:comentario_pk>',views.comentarioDelete,name="comentario_delete"),
    path('comentario_edit/<int:comentario_pk>',views.comentario,name="comentario"),
    path('comentario_edit/comentario_update',views.comentarioUpdate,name="comentario_update"),
    path('login',LoginView.as_view(template_name='tienda/login.html'),name="login")
]
#<!--{% url 'comentarioDelete' comentario_pk=comentario.id juego_pk=juego.id %}-->