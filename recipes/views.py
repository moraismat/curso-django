from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
from django.http import Http404

# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        is_published=True,
        category__id=category_id
    ).order_by('-id')

    if not recipes:
        raise Http404('Not Found')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,        
        'title': f'{recipes.first().category.name} - Category | '
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })