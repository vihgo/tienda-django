from django.shortcuts import render,redirect
from .models import Juego,Comentario

# Create your views here.
def index(request):
    juegos= Juego.objects.all()
    context={"RPG":juegos}
    return render(request,'tienda/index.html',context)

def comentario(request,comentario_pk):
    comentario=Comentario.objects.get(id=comentario_pk)
    juego=comentario.juego
    context={"juego":juego, "comentario":comentario}
    return render(request,'tienda/comentario.html',context)

def comentarioUpdate(request):
    comentario=Comentario.objects.get(id=request.POST["comentario_id"])
    comentario.nombre=request.POST["nombre"]
    comentario.email=request.POST["email"]
    comentario.comentario=request.POST["comentario"]
    comentario.save()
    context={"juego":comentario.juego, "comentario":comentario}
    return render(request,'tienda/comentario.html',context)



def comentarioDelete(request,comentario_pk):

    comentario=Comentario.objects.get(id=comentario_pk)
    comentario.delete() 
    return render(request,'tienda/comentario.html')


    

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