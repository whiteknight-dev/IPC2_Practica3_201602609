from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('borrar/', views.borrar, name='borrar'),
  path('cargar/', views.cargar, name='cargar'),
  path('procesamiento/', views.procesamiento, name='procesamiento'),
  path('procesar/', views.procesar, name='procesar'),
  path('datos', views.datos, name='datos')
]