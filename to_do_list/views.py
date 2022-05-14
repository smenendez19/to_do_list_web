from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from .models import Tarea
from .forms import TareaCreateForm
from django.core.paginator import Paginator
import json
from django.core import serializers
from .serializers import TareaSerializer
from django.template import loader

# Filtrado y Ordenado de la lista de tareas (GET)
def filter_and_order_tasks(request):
    def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    tareas_status = ""
    tareas_order = ""
    if is_ajax(request) and request.method == "GET":
        # Filtrado de tareas
        if 'filter' in request.GET:
            tareas_status = request.GET.get('filter')
            if tareas_status == 'all':
                list_tareas = Tarea.objects.filter(usuario=request.user.id)
            elif tareas_status == 'true':
                list_tareas = Tarea.objects.filter(usuario=request.user.id, estado__in=[True])
            elif tareas_status == 'false':
                list_tareas = Tarea.objects.filter(usuario=request.user.id, estado__in=[False])
        else:
            list_tareas = Tarea.objects.filter(usuario=request.user.id)
        # Ordenamiento por fecha
        if 'order' in request.GET:
            tareas_order= request.GET.get('order')
            if tareas_order == 'ascended':
                list_tareas = list_tareas.order_by('created')
            elif tareas_order == 'descended':
                list_tareas = list_tareas.order_by('-created')
        list_tareas = TareaSerializer(list_tareas, many=True).data
        return JsonResponse(list_tareas, status=200, safe=False)

# Pagina de Inicio

def home(request):
    if not request.user.is_authenticated:
        return redirect('accounts_login')
    if request.method == "POST":
        if "change_estado_tarea" in request.POST:
            tarea_id = request.POST.get("change_estado_tarea")
            tarea_edit = Tarea.objects.get(id=tarea_id)
            tarea_edit.estado = not tarea_edit.estado
            tarea_edit.save()
        if "delete_tarea" in request.POST:
            tarea_id = request.POST.get("delete_tarea")
            tarea_delete = Tarea.objects.get(id=tarea_id)
            tarea_delete.delete()
        if "edit_tarea" in request.POST:
            tarea_id = request.POST.get("edit_tarea")
            request.session['tarea_id'] = tarea_id
            return redirect('tarea_edit')
    # Filtrado de tareas
    tareas_status = ""
    if 'filter' in request.GET:
        tareas_status = request.GET.get('filter')
        if tareas_status == 'all':
            list_tareas = Tarea.objects.filter(usuario=request.user.id)
        elif tareas_status == 'true':
            list_tareas = Tarea.objects.filter(usuario=request.user.id, estado__in=[True])
        elif tareas_status == 'false':
            list_tareas = Tarea.objects.filter(usuario=request.user.id, estado__in=[False])
    else:
        list_tareas = Tarea.objects.filter(usuario=request.user.id)
    # Ordenamiento por fecha
    tareas_order = ""
    if 'order' in request.GET:
        tareas_order= request.GET.get('order')
        if tareas_order == 'ascended':
            list_tareas = list_tareas.order_by('created')
        elif tareas_order == 'descended':
            list_tareas = list_tareas.order_by('-created')
    # Paginado
    page_number = request.GET.get('page')
    tareas_pages = Paginator(list_tareas, 9)
    tareas_pages_obj = tareas_pages.get_page(page_number)
    return render(request, "to_do_list/home_ajax.html", {"list_tareas" : tareas_pages_obj, 'order' : tareas_order, 'filter' : tareas_status})

# Creacion de nueva tarea

def tarea_create(request):
    if not request.user.is_authenticated:
        return redirect('accounts_login')
    if request.method == "POST":
        new_tarea = Tarea(usuario=request.user)
        new_tarea = TareaCreateForm(request.POST, instance=new_tarea)
        if new_tarea.is_valid:
            new_tarea.save()
        if 'save_tarea' in request.POST:
            return redirect('home')
        elif 'save_and_create_another' in request.POST:
            pass
    form_create = TareaCreateForm()
    return render(request, "to_do_list/tarea_create.html", {"form_create" : form_create})

# Edicion de una tarea existente

def tarea_edit(request):
    if not request.user.is_authenticated:
        return redirect('accounts_login')
    if request.method == "POST":
        tarea_id = request.POST.get("save_tarea")
        updated_tarea = Tarea.objects.get(id=tarea_id)
        form_edit = TareaCreateForm(request.POST, instance=updated_tarea)
        if form_edit.is_valid:
            form_edit.save()
        return redirect('home')
    tarea_id = request.session.get('tarea_id')
    tarea_edit = Tarea.objects.get(id=tarea_id)
    form_edit = TareaCreateForm(None, instance=tarea_edit)
    return render(request, "to_do_list/tarea_edit.html", {"form_edit" : form_edit, "tarea_id" : tarea_id})