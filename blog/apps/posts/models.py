from django.db import models
from django.utils import timezone
# Create your models here.
import random
import os
from functools import partial


#Categoria:
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre
    
# Post
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='post', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parent = False):
            self.imagen.delete(self.imagen.name)
            super().delete()
    
# Articulo
def get_random_avatar_filename(instance, filename):
    return f'articulo/avatars/{filename}'

def default_avatar():
    return 'articulo/avatar/avatar3_default.jpg'

class Articulo(models.Model):
    # Campos existentes
    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/default_articulo.jpg')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    publicado = models.DateTimeField(default=timezone.now)
    
    # Nuevos campos
    avatar = models.ImageField(null=True, blank=True, upload_to=get_random_avatar_filename, default=default_avatar)
    nickname = models.CharField(max_length=30, default="Sin Nickname")


    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parent=False):
        self.imagen.delete()

        if self.avatar: 
            self.avatar.delete()
        super().delete(using=using, keep_parent=keep_parent)
        # super().delete()




# class Comentario:

#     def __init__(self, id_articulo, id_usuario, contenido):
#         self.id = Comentario.id_counter
#         Comentario.id_counter += 1
#         self.id_articulo = id_articulo
#         self.id_usuario = id_usuario
#         self.contenido = contenido
#         self.fecha_hora = datetime.now()
#         self.estado = 'activo'

# -------------------------------------------
# class Comentario:

#     def __init__(self, id_articulo, id_usuario, contenido):
#         self.id = Comentario.id_counter
#         Comentario.id_counter += 1

#         self.id_articulo = id_articulo
#         self.id_usuario = id_usuario
#         contenido = models.TextField(null=False)
#         fecha = models.DateTimeField(auto_now_add=True)
#         estado = models.BooleanField(default=True)



# from django.contrib.auth.models import User

# class Comentario(models.Model):
#     id_articulo = models.ForeignKey('Articulo', on_delete=models.CASCADE)
#     id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     contenido = models.TextField(null=False)
#     fecha = models.DateTimeField(auto_now_add=True)
#     estado = models.BooleanField(default=True)

#     def __str__(self):
#         return f"Comentario {self.id} - Artículo {self.id_articulo_id} - Usuario {self.id_usuario_id}"




# -------------------------los que me fatan-----------
# class Usuario(models.Model):
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     telefono = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
#     contraseña = models.CharField(max_length=100)
#     fecha_registro = models.DateTimeField(auto_now_add=True)
#     avatar = models.ImageField(upload_to='avatars/', default='default_avatar.png')
#     estado = models.CharField(max_length=100, default='offline')

#     def login(self):
#         # Código para el inicio de sesión
#         self.estado = 'online'
#         print(f"Bienvenidx, {self.username}!")

# class Publico(Usuario):
#     es_publico = models.BooleanField(default=True)

#     def comentar(self, articulo, comentario):
#         # Código para el comentario de usuario rol público
#         if articulo.estado == 'activo':
#             comentario_obj = Comentario(articulo=articulo, usuario=self, contenido=comentario)
#             comentario_obj.save()
#             print(f"{self.username}: \"{comentario_obj.contenido}\"")
#         else:
#             print("No se puede comentar en un artículo inactivo.")

# class Colaborador(Usuario):
#     es_colaborador = models.BooleanField(default=True)

#     def comentar(self, articulo, comentario):
#         # Código para el comentario de colaborador
#         if articulo.estado == 'activo':
#             comentario_obj = Comentario(articulo=articulo, usuario=self, contenido=comentario)
#             comentario_obj.save()
#             print(f"{self.username}: \"{comentario_obj.contenido}\"")
#         else:
#             print("No se puede comentar en un artículo inactivo.")


# class Comentario(models.Model):
#     id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     contenido = models.TextField()
#     fecha_hora = models.DateTimeField(auto_now_add=True)
#     estado = models.CharField(max_length=100, default='activo')
