"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from mi_pagina.views import home
from directivos.views import add_directivo
from empleados.views import add_empleado
from productos.views import add_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('directivos/add/', add_directivo, name='add_directivo'),
    path('empleados/add/', add_empleado, name='add_empleado'),
    path('productos/add/', add_producto, name='add_producto'),
]
