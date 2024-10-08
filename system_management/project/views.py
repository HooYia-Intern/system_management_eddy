from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from.forms import ProjectFileForm
from .models import Project, ProjectNote
# Create your views here.
@login_required 
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'project/projects.html',{
        'projects': projects
    })
 
@login_required
def project(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    return render(request, 'project/project.html',{
        'project': project
    })

@login_required
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description  = request.POST.get('description', '')

        if name:
            Project.objects.create(name=name, description=description, created_by=request.user )

            return redirect('/projects/')
        else:
            print('not valide project')


    return render(request, 'project/add.html')

@login_required
def edit(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description  = request.POST.get('description', '')

        if name:
            project.name = name
            project.description = description
            project.save()

            return redirect('/projects/')
        
    return render(request, 'project/edit.html',{
        'project': project
    })



@login_required
def delete(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    project.delete()

    return redirect('/projects/')


@login_required

def upload_file(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    

    if request.method == 'POST':
        form = ProjectFileForm(request.POST , request.FILES )

        if form.is_valid():
            projectfile = form.save(commit=False)
            projectfile.project = project
            projectfile.save()
            return redirect (f'/projects/{project_id}/')
    else:
        form = ProjectFileForm
    

        


    form = ProjectFileForm()


    return render(request, 'project/upload_file.html', {
        'project': project,
        'form': form,
    })


# notes

@login_required

def add_note(request,project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        body = request.POST.get('body', '')

        if name and body:
            ProjectNote.objects.create(name=name, body=body, project=project)


    return render(request, 'project/add_note.html',{
        'project': project
    })


