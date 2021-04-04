from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Formulario de creacion de nuevo usuario

class UserSignUpForm(UserCreationForm):
    dicc_errors = {
        'required' : ("El campo es requerido"),
        'invalid' : ("Ingrese un valor valido para el campo"),
        'max_length' : "No debe superar el maximo de 50 caracteres en el campo",
        'empty_value' : "El campo esta vacio",
    }
    error_messages = {
        'password_mismatch' : "Las dos Contraseñas no coinciden",
    }
    username = forms.CharField(label=("Usuario"), 
                            required=True, 
                            max_length=50, 
                            help_text="Ingrese un nombre para su cuenta, maximo 50 caracteres, no incluya espacios, solo letras, numeros o signos y guiones",
                            error_messages=dicc_errors)
    email = forms.EmailField(label="EMail", 
                            required=True, 
                            widget=forms.EmailInput,
                            help_text="Debe ser un mail valido (@outlook.com, @gmail.com, @yahoo.com)",
                            error_messages=dicc_errors)
    password1 = forms.CharField(label=("Contraseña"), 
                            required=True, 
                            widget=forms.PasswordInput, 
                            help_text="Ingrese la Contraseña, debe tener al menos 8 caracteres y no debe tener letras/numeros consecutivos ni informacion similar a la ingresada.",
                            error_messages=dicc_errors)
    password2 = forms.CharField(label=("Confirmacion de Contraseña"), 
                            required=True, 
                            widget=forms.PasswordInput, 
                            help_text=("Confirme la misma Contraseña ingresada"),
                            error_messages=dicc_errors)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.set_password(self.cleaned_data["password2"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
