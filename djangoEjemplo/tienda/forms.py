from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
     email= forms.EmailField(required='True',widget=forms.EmailInput(attrs={'class': 'input is-primary', 'placeholder': 'Correo electrónico'}))
     

     class Meta:
          model=User
          fields=['username','email','password1','password2']
          widgets= {
               'password1': forms.PasswordInput(attrs={'class': 'input is-primary', 'placeholder': 'pedrito@gmail.com'}),
               'password2': forms.PasswordInput(attrs={'class': 'input is-primary', 'placeholder': 'asd123'}),
               'username': forms.TextInput(attrs={'class':'input is-primary','placeholder': 'Pedro'}), 
               #'email': forms.EmailInput(attrs={'class': 'input is-danger', 'placeholder': 'asd123'}),
               

            }
          labels= {
                'username': 'Nombre de usuario',
                'email': 'Correo electrónico',
                'password1': 'Contraseña',
                'password2': 'Confirmar contraseña'
            
          }
