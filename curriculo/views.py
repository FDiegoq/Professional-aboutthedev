from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    cursos=Curso.objects.all()
    skills=Habilidade.objects.all()
    context={
        'cursos':cursos,
        'skills':skills
    }
    return render(request, 'curriculo/index.html', context)
