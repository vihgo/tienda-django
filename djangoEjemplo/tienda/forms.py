from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
     username= forms.CharField(max_length=100,widget=forms.EmailInput(attrs={'class': 'input is-primary', 'placeholder': 'Diego'}))
     email= forms.EmailField(required='True',widget=forms.EmailInput(attrs={'class': 'input is-primary', 'placeholder': 'Correo electrónico'}))
     password1= forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'input is-primary'}))
     password2= forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'input is-primary'}))
    
     class Meta:
          model=User
          fields=['username','email','password1','password2']
          labels= {
                'username': 'Nombre de usuario',
                'email': 'Correo electrónico',
                'password1': 'Contraseña',
                'password2': 'Confirmar contraseña'
            
          }
