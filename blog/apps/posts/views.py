from django.shortcuts import render
from .models import Articulo, Post
from django.views import View


# Create your views here.


def posts(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts' : posts})

# # Vista basada en funcion
# def articulos(request):
#     articulos = Articulo.objects.all()
#     return render(request, 'articulo.html', {'articulos' : articulos})



# vista basada en clases
class ArticuloView(View):
    template_name= 'articulo.html'

    def get(self, request):
        articulos = Articulo.objects.all()
        return render(request, 'articulo.html', {'articulos' : articulos})


def existe_articulo(id):
    for i in Articulo:
        if i.id == id:
            return i
    return None

def leer_articulo(request, id):
    articulo = Articulo.objects.filter(id = id).first()
        


    context = {
        'articulos': articulo,
    }

    return render (request, 'articulo_individual.html', context)

