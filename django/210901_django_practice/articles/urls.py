from django.urls import path
from . import views

app_name = 'articles'   # templates/articles와 같이 해줄 떄 같이

urlpatterns = [
    path('index/', views.index),
    path('', views.index),  # ''는 기본주소 -> https://127.0.0.1:8000/articles/ 주소를 의미
]
