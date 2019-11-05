from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Like,Comment, User
import operator
from django.contrib.auth.decorators import login_required
from .forms import PostForm

def main(request):
    posts=Post.objects.all()#2줄
    sort=request.GET.get('sort','')


    try:
        liked_post=Like.objects.filter(user=request.user).values_list('post__id', flat=True)
    except:
        liked_post=None

    return render(request, 'insta/main.html',{
        'posts':posts,
        'liked_post':liked_post
        })

def count(request):
    posts=Post.objects.all()

    return render(request, 'insta/count.html',{'posts':posts})

def like(request, post_pk):
    post= get_object_or_404(Post, pk=post_pk)

    if request.method =='POST':
        
            Like.objects.create(user=request.user, post=post)

    return redirect('main')
    