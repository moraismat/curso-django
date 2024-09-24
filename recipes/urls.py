from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="recipes-home"),
    path('recipes/<int:id>/', recipe, name="recipes-recipe"),
]
