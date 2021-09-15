# README-김현규

### 개요

- django form과 bootstrap을 활용하여 영화 게시판의 CRUD 구현



### 기본 설정

- 기본적인 설정은 pjt04와 비슷하므로 중복되는 부분의 설명은 생략하겠음

- 이번에는 페어프로그래밍으로 진행함
- gitlab에 프로젝트를 생성하고 팀원을 등록하여 진행
- 이 때 아직 db관련된 설정을 익히지 못했으므로 gitignore에서 db.sqlite3는 주석처리하여 공유



### Form

```python
# movies/forms.py
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

```

- 위의 코드처럼 django의 forms.ModelForm을 상속하여 MovieForm 클래스를 만들었다. MovieForm의 하위클래스인 Meta 클래스에서 model과 fields 설정을 통해서 model의 정보를 불러와서 사용하였다.



### View

```python
# movies/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Movie
from .forms import MovieForm
# Create your views here.

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)

@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()

    return redirect('movies:index')
```

- 지난 pjt04와는 다르게 form을 이용해서 view를 구성해서 약간 복잡했지만 작동 원리를 이해하고 나니 편리하게 코드를 작성할 수 있었다.
- 데코레이터 사용을 통해 함수의 기능을 추가하는 부분이 재미있었습니다.



#### 소감

페어프로그래밍을 통해서 팀원과 함께 프로젝트를 진행하는 것이 참 재미있었습니다. 이를 통해 서로가 가진 지식을 나누고 팀프로젝트를 할 때 서로를 배려해서 프로젝트가 잘 진행될 수 있도록 하는 방법을 배울 수 있는 자리였던것 같습니다. 또한 코드적으로 이번 주는{% include %}를 통해서 html 파일에서 다른 html 파일을 불러 오는 기능이나, 데코레이터와 같은 파이썬의 문법을 새롭게 적용해 볼 수 있어서 재밌었습니다. 앞으로도 더 다양한 팀프로젝트를 할 수 있을 것이라 생각해서 기대하고 있습니다.

