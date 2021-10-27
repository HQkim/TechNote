from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artist_list),
    path('artists/<artist_pk>/', views.artist_detail),
    path('artists/<artist_pk>/music/', views.artist_music),
    path('music/', views.music_list),
    path('music/<music_pk>/', views.music_detail),
]