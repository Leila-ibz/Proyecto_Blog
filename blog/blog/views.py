from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView



# def index(request):
#     return render(request, 'index.html')

class Indexviews(TemplateView):
   template_name = 'index.html'

def quienes_somos_view(request):
   return render(request, 'quienessomos.html')