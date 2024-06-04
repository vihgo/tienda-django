from django.shortcuts import render
from .models import Juego

# Create your views here.
def index(request):
    juegos= Juego.objects.filter(categoria=1).values()
    context={"RPG":juegos}
    return render(request,'tienda/index.html',context)

def juego(request):
    idx=request.GET['juegoId']
    print(idx)
    juego= Juego.objects.get(id=idx)
    context={"juego":juego}
    return render(request,'tienda/juego.html', context)
    
    