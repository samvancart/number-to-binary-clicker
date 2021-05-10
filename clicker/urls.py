from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:number>/num_clicked', views.num_clicked, name='num_clicked'),
]