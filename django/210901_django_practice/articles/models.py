from django.db import models

# Create your models here.


class Article(models.Model):
    # id (Primary Key 생략)
    # id = models.AutoField(primary_key=Ture) 1, 2, 3, 4...

    # max_length 필수 -> 위젯에서 중요 (클래스 변수 - 공유)
    title = models.CharField(max_length=10)
    content = models.TextField()             # max_length 옵션
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
