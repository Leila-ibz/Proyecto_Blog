
from django.db import models

class articulo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

class comentario(models.Model):
    article = models.ForeignKey(articulo, on_delete=models.CASCADE, related_name='comentarios')
    author = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
