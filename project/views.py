from django.shortcuts import render
from project.models import Project


def index(request):
    projects = Project.objects.all()

    return render(request, 'project/index.html', {'projects': projects})


def show(request, project_id):
    project = Project.objects.get(pk=project_id)

    return render(request, 'project/show.html', {'project': project})
