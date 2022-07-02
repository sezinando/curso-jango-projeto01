from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', 
    context={'name':'José Roberto',
    'Data':"20 de Janeiro", 'Contato': "02299922992"})