from django.shortcuts import render

from .models import Project


def project_list(request):
    projects = Project.objects.all()
    ctx = {
        'projects': projects
    }
    return render(request, 'diyprojects/project_list.html', ctx)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    ctx = {
        'project': project
    }
    return render(request, 'diyprojects/project_detail.html', ctx)
