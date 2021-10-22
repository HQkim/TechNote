from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Review, Comment
from .forms import ReviewForm, CommentForm
# Create your views here.


@login_required
@require_http_methods(['GET', 'POST'])
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_detail', review.pk)
    else:
        form = ReviewForm()

    context = {
        'form': form,
    }
    return render(request, 'community/create_review.html', context)


@require_safe
def review_index(request):
    reviews = Review.objects.order_by('-pk')

    context = {
        'reviews': reviews,
    }

    return render(request, 'community/review_index.html', context)


@require_safe
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'community/review_detail.html', context)


@require_POST
def create_comment(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
        return redirect('community:review_detail', review.pk)
    return redirect('accounts:login')


@require_POST
def like_review(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like.filter(pk=request.user.pk).exists():
            review.like.remove(request.user)
        else:
            review.like.add(request.user)
        return redirect('community:review_detail', review.pk)
    return redirect('accounts:login')
