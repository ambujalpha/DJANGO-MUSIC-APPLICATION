from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # register
    path('register/', views.UserFormView.as_view(), name='register'),

    # /music/<album_id>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/(update)
    path('<pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    path('<pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]
