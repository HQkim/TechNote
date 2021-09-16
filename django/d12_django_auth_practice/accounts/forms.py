from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model  # 독특한 점. 지금 쓰고 있는 모델의 유저 들고오라.

User = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)
