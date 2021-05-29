from . import views
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [   
    path('', views.base, name='base'),
    path('inicio', views.index, name='index'),
    # path('buscar', views.search, name='search'),

    path('efectivo', views.efectivo, name='efectivo'),
    path('metodosPago', views.metodos_de_pago, name='metodos_pago'),
    path('productos', views.productos, name='productos'),
    path('tarjeta', views.tarjeta, name='tarjeta'),
    path('usuario/login', views.login, name='login'),
    path('usuario/logout', views.logout, name='logout'),
    path('usuario/dashboard', views.dashboard, name='dashboard'),
    # path('usuario/categoria/nueva', views.new_category, name='new_category'),
]
