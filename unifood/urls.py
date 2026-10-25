"""unifood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from cantina.views import home, cadastrar_categoria, listar_produtos, avancar_status_pedido

urlpatterns = [
    path('', home, name='home'),
    path('pedidos/<int:pedido_id>/avancar/', avancar_status_pedido, name='avancar_status_pedido'),

    #Autenticacao
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Telas da Cantina
    path('categoria/nova/', cadastrar_categoria, name='nova_categoria'),
    path('produtos/', listar_produtos, name='produtos'),

    #Admin
    path('admin/', admin.site.urls),
]