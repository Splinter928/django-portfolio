from django.shortcuts import render
from .models import Project
from django.http import HttpResponse


def home(request):
    projects = Project.objects.all()
    return render(request, r'portfolio\home.html', {'projects': projects})
#    return HttpResponse('Hello')
