from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

]
