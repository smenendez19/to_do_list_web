from django import forms
from django.forms import ModelForm
from .models import Tarea

class TareaCreateForm(ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}), required=False)
    
    class Meta:
        model = Tarea
        fields = '__all__'
        exclude = ['usuario', 'created', 'updated']
        labels = {
            "nombre" : "Tarea",
            "descripcion" : "Descripcion detallada de la tarea",
            "estado" : "Estado inicial de la tarea"
        }
        help_texts = {
            "nombre" : "No debe superar los 50 caracteres",
            "descripcion" : "No debe superar los 300 caracteres",
            "estado" : "Completado o no completado"
        }