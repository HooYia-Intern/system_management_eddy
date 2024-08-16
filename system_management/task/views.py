from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from project.models import Project
from todolist.models import Todolist
from .models import Task

# Create your views here.

@login_required
def add(request, project_id, todolist_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        Task.objects.create(name=name, description=description, project=project, todolist=todolist, created_by=request.user)
        return redirect(f'/projects/{project_id}/{todolist_id}')

    return render(request, 'task/add.html', {
        'project': project,
        'todolist': todolist,
    })
