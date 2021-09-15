from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()

            # add_message
            # messages.add_message(request, messages.INFO, '게시글이 잘 작성됨ㅋ')

            # shortcut
            messages.info(request, '게시글 잘 작성됨ㅋㅋ')

            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    messages.add_message(request, messages.WARNING, '게시글이 삭제되었습니다.')
    # messages.warning(request, '게시글이 삭제되었습니다.')

    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.WARNING, '게시글이 삭제되었습니다.')
            messages.warning(request, '게시글이 수정되었습니다.')
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
