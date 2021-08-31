from django.urls import path, include
from . import views

app_name = 'pages'

urlpatterns = [
    # path('', views.index), # 아무것도 안넣으면 기본주소
    path('index/', views.index),
    path('drink/', views.drink),
]
