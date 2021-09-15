from django.urls import path
from . import views

app_name = 'board'

# board/ +
urlpatterns = [
    # create/
    path('create/', views.create, name='create'),

    # board/
    path('', views.index, name='index'),

    # board/1/
    path('<int:question_pk>/', views.detail, name='detail'),

    # board/1/update/
    path('<int:question_pk>/update/', views.update, name='update'),

    # board/1/delete/
    path('<int:question_pk>/delete/', views.delete, name='delete'),
]
