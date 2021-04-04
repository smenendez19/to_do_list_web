from django.urls import path
from to_do_list.views import home, tarea_create, tarea_edit, filter_and_order_tasks

urlpatterns = [
    path('', home, name="home"),
    path('task_create/', tarea_create, name="tarea_create"),
    path('task_edit/', tarea_edit, name="tarea_edit"),
    path('task_filter_order/', filter_and_order_tasks, name = "filter_and_order_tasks")
]
