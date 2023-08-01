
from django.shortcuts import render, redirect
from .models import articulo, comentario
from .forms import articuloForm, comentarioForm

def art_list(request):
    articulo = articulo.objects.all()
    return render(request, 'articulo/art_list.html', {'articulo': art_list})

def art_detalle(request, article_id):
    articulo = articulo.objects.get(id=article_id)
    comentario = articulo.comentario.all()
    return render(request, 'articulo/art_detalle.html', {'articulo': articulo, 'comentario': comentario})

def crear_art(request):
    if request.method == 'POST':
        form = articulo.Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('art_list')
    else:
        form = articulo.Form()
    return render(request, 'articulo/art_form.html', {'form': form})

def create_comen(request, article_id):
    articulo= articulo.objects.get(id=article_id)
    if request.method == 'POST':
        form = comentario.Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.artiulo = articulo
            comment.save()
            return redirect('art_detalle', article_id=article_id)
    else:
        form = comentario.Form()
    return render(request, 'articulo/comentario_form.html', {'form': form})
