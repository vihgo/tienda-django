from django.shortcuts import render
from .models import Juego,Comentario

# Create your views here.
def index(request):
    juegos= Juego.objects.filter(categoria=1).values()
    context={"RPG":juegos}
    return render(request,'tienda/index.html',context)

def juego(request):
    

    if request.method !="POST":
        idx=request.GET['juegoId']
        juego= Juego.objects.get(id=idx)
        context={"juego":juego}
        
    else:
        idx=request.POST['juegoId']
        print(idx)
        juego= Juego.objects.get(id=idx)
        comentario=request.POST['comentario']
        nombre=request.POST['nombre']
        email=request.POST['email']
        objComentario= Comentario.objects.create(nombre=nombre,comentario=comentario,email=email,juego=juego)
        objComentario.save()
        context={"juego":juego, "comentario":objComentario}
    
    return render(request,'tienda/juego.html', context)