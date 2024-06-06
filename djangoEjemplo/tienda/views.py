from django.shortcuts import render
from .models import Juego,Comentario

# Create your views here.
def index(request):
    juegos= Juego.objects.filter(categoria=1).values()
    context={"RPG":juegos}
    return render(request,'tienda/index.html',context)

def comentarioDelete(request,comentario_pk, juego_pk):
    context={}

    comentario=Comentario.objects.get(id=comentario_pk)
    comentario.delete() 
    juego= Juego.objects.get(id=juego_pk)
    comentario=juego.comentarios.all().values()
    context={"juego":juego, "comentarios":comentario}
    return render(request,'tienda/juego.html',context)


    

def juego(request):
    

    if request.method !="POST":
        idx=request.GET['juegoId']
        juegox= Juego.objects.get(id=idx)
        objComentario=juegox.comentarios.all().values()
        print("objComentario")
        print(objComentario)
        context={"juego":juegox, "comentarios":objComentario}
        
    else:
        idx=request.POST['juegoId']
        print(idx)
        juego= Juego.objects.get(id=idx)
        comentario=request.POST['comentario']
        nombre=request.POST['nombre']
        email=request.POST['email']
        objComentario= Comentario.objects.create(nombre=nombre,comentario=comentario,email=email,juego=juego)
        objComentario.save()
        objComentario=juego.comentarios.all().values()
        context={"juego":juego, "comentarios":objComentario}
    
    return render(request,'tienda/juego.html', context)