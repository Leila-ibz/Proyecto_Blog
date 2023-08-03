from django.shortcuts import render
from .models import Articulo, Post, Categoria
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
#Mostrar artículos
class ArticuloView(View):
    template_name= 'articulo.html'
#Obtener parametro para filtrar por categorías, mediante url
    def get(self, request):
        categoria_id = request.GET.get("categoria_id",None)
        if categoria_id == None:
            articulos = Articulo.objects.all()
        else:
            articulos = Articulo.objects.filter(categoria__id = categoria_id)
        
        opciones_dropdown = Categoria.objects.all()
        return render(request, 'articulo.html', {'articulos' : articulos ,'opciones_dropdown' : opciones_dropdown, 'categoria_filtrada': categoria_id},)


        

#Mostrar categorías
def mostrar_articulos(request):
    categorias = Categoria.objects.all()
    return render(request, 'articulo.html', {'categorias': categorias})

def existe_articulo(id):
    for i in Articulo:
        if i.id == id:
            return i
    return None

def dropdown_menu_view(request):
    # Aquí puedes agregar la lógica para obtener las opciones del dropdown
    opciones_dropdown = ['Opción 1', 'Opción 2', 'Opción 3']

    return render(request, 'articulo.html', {'opciones_dropdown': opciones_dropdown})


def leer_articulo(request, id):
    articulo = Articulo.objects.filter(id = id).first()
        


    context = {
        'articulos': articulo,
    }

    return render (request, 'articulo_individual.html', context)

