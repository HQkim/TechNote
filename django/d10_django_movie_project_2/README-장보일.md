# DB를 활용한 웹 페이지 구현

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



 



