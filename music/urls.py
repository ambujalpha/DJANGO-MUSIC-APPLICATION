from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    path('', views.index, name='index'),

    # /music/<album_id>/
    path('<int:album_id>/', views.detail, name='detail'),

    # /music/<album_id>/favourite
    path('<int:album_id>/favourite/', views.favourite, name='favourite'),
]