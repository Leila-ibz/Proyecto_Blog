"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
# from .views import index
from .views import Indexviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Esto hice para que muestre las imagenes
from django.conf import settings
from django.conf.urls.static import static
from . import views


# ACA LE AVISA QUE TIENE QUE IR A BUSCAR LA URL DE LA APLICACION

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Indexviews.as_view(), name='index'),
    path('', include('apps.posts.urls')),
    path('', include('apps.contacto.urls')),
    # path('apps/', include('apps.urls', namespace='apps')),
    path('quienessomos/', views.quienes_somos_view, name='quienes_somos')
    # path('', include('apps.posts.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Esto hice para que muestre las imagenes

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)