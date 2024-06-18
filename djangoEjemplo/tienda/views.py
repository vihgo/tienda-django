from django.shortcuts import render,redirect
from .models import Juego,Comentario
from django.contrib.auth.views import logout_then_login
from .forms import *
# Create your views here.

def agregarAlCarro(request,juego_id):
    carro=request.session.get("carro",[]) #intenta obtener la variable carro de la session, si no existe la crea
    juego= Juego.objects.get(id=juego_id)
    productoEnCarro=False
   
    for juego_carro in carro:
        if juego_carro['id']==juego_id:
            productoEnCarro=True
            juego_carro['cantidad']+=1
            juego_carro['total']=juego_carro['cantidad']*juego_carro['precio']
            break
    
    if productoEnCarro==False:
        carro.append({"id":juego_id,"categoria":juego.categoria.nombre,"precio":juego.precio,"nombre":juego.nombre,"src_image":juego.srcImage,"cantidad":1,"total":juego.precio*1})
    total=0
    for juego_carro in carro:
        total+=juego_carro['total']
        request.session["total_carro"]=total

    request.session["carro"]=carro
    #objComentario=juegox.comentarios.all().values()
    context={"juego":juego, "tamaño_carrito":len(carro)}
    return render(request,'tienda/juego.html', context)

def carro(request):
    
    carro=request.session.get("carro",[]) #intenta obtener la variable carro de la session, si no existe la crea
    #carro.append([juego_id,juego.precio,juego.nombre,juego.srcImage,1,juego.precio*1])
    context={"carro":carro, "total_carro":request.session.get("total_carro",0)}
    print(carro)
    return render(request,'tienda/carrito.html', context)

def index(request):
    juegos= Juego.objects.all()
    context={"juegos":juegos}
    return render(request,'tienda/index.html',context)

def registro(request):

    if request.method=='POST':
        registro=RegistroForm(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to='login')
    else:
        registro= RegistroForm()

    return render(request, 'tienda/registro.html',{'form':registro})

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

def logut(request):
    return logout_then_login(request,login_url="login")
    


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