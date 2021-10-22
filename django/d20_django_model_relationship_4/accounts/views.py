from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
# Create your views here.


@require_http_methods(['GET', 'POST'])
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('community:review_index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('community:review_index')


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:review_index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'community:review_index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('community:review_index')


@require_safe
def profile(request, username):
    profile = get_object_or_404(get_user_model(), username=username)
    is_following = profile.followers.filter(pk=request.user.pk).exists()
    context = {
        'profile': profile,
        'is_following': is_following,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, username):
    if request.user.is_authenticated:
        follower = request.user
        profile = get_object_or_404(get_user_model(), username=username)
        if profile.followers.filter(pk=follower.pk).exists():
            profile.followers.remove(follower)
        else:
            profile.followers.add(follower)
        return redirect('accounts:profile', profile.username)

    return redirect('accounts:login')
