from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    updated = serializers.DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    class Meta:
        model = Tarea
        fields = [
            "id",
            "nombre",
            "descripcion",
            "usuario",
            "estado",
            "created",
            "updated"
        ]