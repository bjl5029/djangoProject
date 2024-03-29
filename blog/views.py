from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

#
# def index(request):
#     posts = Post.objects.all().order_by('-id')
#     return render(request, 'blog/index.html',
#                   {
#                       'posts': posts,
#                   })

class PostList(ListView):
    model = Post
    template_name = "blog/index.html"

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request, 'blog/single_post_page.html', {'post': post, }
    )
