# README

## README-장보일

### 1. 목표

- 데이터 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework 를 통한 데이터 조작

### 2. 내용

앞선 프로젝트와 비슷한 내용은 생략하도록 하겠습니다. 

#### 1. FORM

```python
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

```

#### 2. MODEL

```python
from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.pk}번: {self.title}'
```

#### 3. views.py

```python
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



  view.py에서 데코레이터와 if문을 통해 DB에 변동을 주는 사항에 있어서 CSRF 토큰을 사용하고 POST 형식으로만 작동이 되게 코드를 작성했습니다. 또한 forms.py를 작성하여 html에서 간단하게 form을 사용할 수 있도록 하며 동시에  데이터 유효성 검증을 진행할 수 있도록 했습니다.



### 3. 어려운점 및 느낀점

  form을 활용하여 데이터를 검증하고 POST와 GET 방식의 차이를 이해하는데 조금 시간이 걸렸지만 교수님들께서 잘 설명해 주신 부분을 직접 페어와 실습을 하며 익숙해지고 이해할 수 있었습니다. 특히나, 앞으로의 프로젝트를 진행할 떄에 내 코드가 더욱 단단해지게 짤 수 있도록 하는 방안들도 알려주셨기에 앞으로 진행하면서 코드를 짜는 방법을 숙지함을 물론 더 잘 짜는 방법에 대해서도 고민해야겠다는 생각을 하게 되었습니다. 

  이제는 반복을 통해 어느정도 django를 활용할 수 있지만 아직은 CSS를 활용하거나 bootstrap을 통해 깔금하게 styling을 하지 못하기에 좀 더 노력해봐야겠습니다.





## README-김현규

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





