from django.shortcuts import render

# Create your views here.


def create(request):

    pass


def index(request):

    return render(request, 'community/index.html')


def detail(request, review_pk):
    pass


def update(request, review_pk):
    pass


def delete(request, review_pk):
    pass
