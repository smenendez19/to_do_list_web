from django.urls import path
from to_do_list.views import home, tarea_create, tarea_edit

urlpatterns = [
    path('', home, name="home"),
    path('tarea_create/', tarea_create, name="tarea_create"),
    path('tarea_edit/', tarea_edit, name="tarea_edit"),
]
