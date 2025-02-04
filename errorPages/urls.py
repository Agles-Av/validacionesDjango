"""
URL configuration for errorPages project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from appAgles.views import index
from appAgles.views import user
from appAgles.views import generar_error_500
from appAgles.views import onepage
from appAgles.views import busqueda
from appAgles.views import error_logs
from appAgles.views import get_error_logs
from django.urls import path, include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('user/', user , name = 'user'),
    path('error/', generar_error_500, name = '500'),
    path('onepage/', onepage, name = 'onepage'),
    path('search/', busqueda, name = 'search'),
    path('error_logs/', error_logs, name = 'error_logs'),
    path('get_error_logs/', get_error_logs, name = 'get_error_logs'),
    path('users/', include('users.urls')),
]



