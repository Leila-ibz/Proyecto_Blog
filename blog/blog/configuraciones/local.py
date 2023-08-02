from .settings import *
#DB Leila SQL
# DATABASES = { 
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'blogdb',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',  
#         'PORT': '3306',        
#     }
# }

#DB Neko Local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Ruta a tu archivo de base de datos SQLite.
    }
}