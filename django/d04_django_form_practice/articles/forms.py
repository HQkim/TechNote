from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:  # form에 대한 정보
        model = Article
        fields = '__all__'
        # fields = ('title', 'content') # 전부 다 적어주는 걸 권장함, 리스트도 가능
        # exclude = ('title',)
        # exclude -> title 빼고
        # 참고로 ('title') -> 문자열이다. ('title') == 'title' 튜플로 쓰려면 ,를 찍어줘야함!
