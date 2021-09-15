from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # Django가 자동으로 입력, 수동 입력 및 수정x
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title
