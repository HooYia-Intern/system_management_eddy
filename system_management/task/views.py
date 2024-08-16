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


@login_required

def detail(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)

    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)

    if request.GET.get('is_done', '') == 'yes':
        task.is_done = True
        task.save()


    return render(request, 'task/detail.html',{
        'task':task,
    })


@login_required
def edit(request, project_id, todolist_id, pk):
    # Fetching the related project and todolist
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)

    # Fetching the specific task to edit
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            task.name = name
            task.description = description
            task.save()

            # Redirect after successfully saving the changes
            return redirect(f'/projects/{project_id}/{todolist_id}/{pk}')

    # Rendering the edit form if the request method is GET or POST fails validation
    return render(request, 'task/edit.html', {
        'task': task
    })