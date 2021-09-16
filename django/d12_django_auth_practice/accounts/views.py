from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm
from IPython import embed
# Create your views here.


@require_http_methods(['GET', 'POST'])
def signup(request):    # User를 Create
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)   # UserCreationForm은 get_user() 메서드가 없음
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):  # Session을 Create
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        # 어떤 유저인지 중요해서 request넣어줌
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # request.user는 검증이 안되어 있음. form.get_user()는 검증되어 있음.
            # https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#writing-an-authentication-backend
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or
                            'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


def logout(request):        # Session을 Delete
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()     # 비밀번호와 session이 연동되어 있어서 비밀번호 바꾸면 세션도 삭제됨
            update_session_auth_hash(request, user)  # request는 웹상, user는 DB 일치
            # embed()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)
