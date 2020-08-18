"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views #importou views de core



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<int:idade>', views.hello),
    path('soma/<int:n1>/<int:n2>', views.soma)
]
#esse path('hello/',) tem que retornar pra algum metodo que retorna algo na tela
#esse metodo vamos criar no view do core
#quando alguem acessa o /hello chame a função views.hello 
