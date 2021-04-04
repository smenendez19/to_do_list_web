from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre", "estado", "created", "updated")
    search_fields = ("nombre", "estado","usuario","created","updated")
    list_filter = ("usuario", "estado", "created", "updated")
    date_hierarchy = "created"

admin.site.register(Tarea, TareaAdmin)