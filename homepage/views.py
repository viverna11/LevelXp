from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'homepage/post_detail.html', context)