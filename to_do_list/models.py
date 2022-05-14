#from django.db import models
from djongo import models
import uuid
from django.contrib.auth.models import User

class Tarea(models.Model):
    #id = models.ObjectIdField(primary_key=True)
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, null=False, blank=False, default="")
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    estado = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "tarea"
        verbose_name_plural = "tareas"
        ordering = ("nombre", "estado", "created", "updated")

    def __str__(self):
        return str(self.nombre)
