from django.shortcuts import render
from .models import  Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    );

def views_single_page(request, pk):
    post = Post.objects.get(pk=pk)


    return render(
        request,
        'blog/views_single_page.html',
        {
            'post': post,
        }
    );