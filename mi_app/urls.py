from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('tienda/', views.tienda, name='tienda'),
]