from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request): 
    return render(request, 'recipes/home.html', context={
        'name': 'Matheus Morais'
    })

def contato(request): 
    return HttpResponse('contato')

def my_view(request): 
    return HttpResponse('Ola Mundo')