from django.shortcuts import render
from .models import Juego,Comentario

# Create your views here.
def index(request):
    juegos= Juego.objects.all()
    context={"RPG":juegos}
    return render(request,'tienda/index.html',context)

def comentarioDelete(request,comentario_pk):

    comentario=Comentario.objects.get(id=comentario_pk)
    juego=comentario.juego
    comentario.delete() 
    comentarios=Comentario.objects.filter(juego=juego)
    context={"juego":juego, "comentarios":comentarios}
    return render(request,'tienda/juego.html',context=context)


    

def juego(request):
    

    if request.method !="POST":
        idx=request.GET['juego_id']
        juego= Juego.objects.get(id=idx)
        comentarios=Comentario.objects.filter(juego=juego)
        #objComentario=juegox.comentarios.all().values()
        context={"juego":juego, "comentarios":comentarios}
        
    else:
        idx=request.POST['juegoId']
        print(idx)
        juego= Juego.objects.get(id=idx)
        comentario=request.POST['comentario']
        nombre=request.POST['nombre']
        email=request.POST['email']
        objComentario= Comentario.objects.create(nombre=nombre,comentario=comentario,email=email,juego=juego)
        objComentario.save()
        #comentarios=juego.comentarios.all().values()
        comentarios=Comentario.objects.filter(juego=juego)
        context={"juego":juego, "comentarios":comentarios}
    
    return render(request,'tienda/juego.html', context)