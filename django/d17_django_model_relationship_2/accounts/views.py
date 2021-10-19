# 장고가 만든 것 (구분하면 좋음)
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, logout as auth_logout

# 우리가 만든 것
from .forms import CustomUserCreationForm

# Create your views here.


def signup(request):
    if request.method == "POST":    # 사용자가 값을 입력했을 때
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:   # GET일 때 => url에 접속했을 때
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()  # form에서 어떤 유저인지 가져오기
            auth_login(request, user)
            return redirect('todos:index')
    else:
        # 위의 CutomUserCreationForm은 model form이라 DB랑 연동되기에 변경해야 하지만 AuthenticationForm은 아니다.
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('todos:index')
