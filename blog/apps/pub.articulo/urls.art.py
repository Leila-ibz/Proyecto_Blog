
from django.urls import path
from . import views

urlpatterns = [
    path('', views.art_list, name='art_list'),
    path('crear/', views.crear_art, name='crear_art'),
    path('<int:article_id>/', views.art_detalle, name='art_detalle'),
    path('<int:article_id>/comentario/', views.crear_comen, name='crear_comen'),
]
