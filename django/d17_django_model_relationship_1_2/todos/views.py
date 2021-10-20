from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import TodoForm


# Create your views here.

@login_required
def index(request):
    # 이코드의 문제 모든 게정의 todo를 서로 볼 수 있음
    # 로그인한 사람의 todo만 보이도록 나중에 수정할 예정
    # todos = Todo.objects.all()

    # 본인이 작성한 todo만 보이도록 설정
    todos = request.user.todo_set.all()

    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)  # 그냥 저장하면 author가 Not Null이기 때문에 에러
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()

    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)
