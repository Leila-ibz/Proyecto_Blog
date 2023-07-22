# URL DE APLICACION


from django.urls import path
from .views import posts, articulos







urlpatterns = [
    path('articulos', articulos, name='articulo'),


]

