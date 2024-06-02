from django.shortcuts import render
from .models import Juego

# Create your views here.
def index(request):
    juegos= Juego.objects.filter(categoria=1).values()
    context={"RPG":juegos}
    return render(request,'tienda/index.html',context)
    