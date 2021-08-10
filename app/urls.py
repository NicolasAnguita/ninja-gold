from django.contrib import admin
from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.index),
    path('process_money', views.procesar),
    path('limpiar', views.limpiar)
]