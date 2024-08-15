from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from.models import Todolist
from project.models import Project
# Create your views here.


@login_required
def add(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')


        if name:
            todolist = Todolist.objects.create( project=project, name=name, description=description, created_by=request.user)

            return redirect(f'/projects/{project_id}/')


    return render(request, 'todolist/add.html')
