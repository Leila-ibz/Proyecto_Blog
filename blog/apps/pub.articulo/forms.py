# articulos/forms.py  
#Los formularios en Django son una forma de gestionar la entrada de datos del usuario y validarlos antes de guardarlos en la base de datos.>
from django import forms
from .models import articulo, comentario

class articuloForm(forms.ModelForm):
    class Meta:
        model = articulo
        fields = ['title', 'content']

class comentarioForm(forms.ModelForm):
    class Meta:
        model =  comentario
        fields = ['author', 'text']


#definimos dos formularios:
#ArticleForm: Es un formulario basado en el modelo Article, que permite a los usuarios crear nuevos artículos.
#CommentForm: Es un formulario basado en el modelo Comment, que permite a los usuarios agregar comentarios a los artículos.