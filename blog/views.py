from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import  Post

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post
    # template_name = 'blog/views_single_page.html'

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