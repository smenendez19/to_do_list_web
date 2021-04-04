from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, default="")
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    #imagen = models.ImageField(upload_to='to_do_list', required=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    estado = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "tarea"
        verbose_name_plural = "tareas"
        #ordering = ("nombre", "estado", "created", "updated")

    def __str__(self):
        return self.nombre
