from django.db import models

# Create your models here.



class Categoria(models.Model):
    nombre=models.CharField(default="default",max_length=50)
    definicion=models.TextField(blank=True)
    
    def __str__(self):
        return str(self.nombre) 

    
class Juego(models.Model):
    nombre= models.CharField(max_length=50)
    preview=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)
    srcImage=models.CharField(default="image" ,max_length=250)
    precio=models.IntegerField(null=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nombre)
    
class Comentario(models.Model):
    nombre= models.CharField(max_length=50)
    comentario= models.CharField(max_length=250)
    email=models.CharField(unique=True,max_length=100)
    juego=models.ForeignKey(Juego, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.email)

class Desarrolladora(models.Model):
    nombre= models.CharField(max_length=50)
    añoFundacion=models.CharField(blank=True, max_length=10)
    historia=models.TextField(blank=True)
    juegos = models.ManyToManyField(Juego, through='DesarrolloJuego')

class DesarrolloJuego(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE)
    fechaLanzamiento=models.CharField(max_length=10)