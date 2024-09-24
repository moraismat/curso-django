from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name="recipes-home"),   
    path('recipes/category/<int:category_id>/', category, name="recipes-category"),
    path('recipes/<int:id>/', recipe, name="recipes-recipe"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)