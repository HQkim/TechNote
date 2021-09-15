from django.db.models import fields
from board.models import Question
from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    # model의 필드와 이름이 같다면, DB에 저장이 된다.
    # form 에서는 min_length 가능
    title = forms.CharField(
        min_length=2,
        max_length=100,
        required=True)
    content = forms.CharField(
        widget=forms.Textarea,
        required=True,
        min_length=2,
        max_length=10000
    )

    # model의 필드가 아니면, HTML + 검증은 하되 저장은 하지 않는다.
    is_save = forms.BooleanField(
        required=False, label='wanna save?', help_text='저장하려면 체크하세요')

    class Meta:
        model = Question
        # 아래 필드는, 모델에 있어야 하며
        # 데이터 검증 + HTML생성을 합니다.
        # fields = ('title', 'content', 'category')
        fields = '__all__'
        # exclude = ('title',)
