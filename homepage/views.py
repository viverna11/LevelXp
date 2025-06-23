from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from . import forms, models


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    def get_queryset(self, request):
        if request.method == 'POST':
            author = request.user
            content = request.POST.get('content')
            comment = Post.objects.create(
                post=Post.objects.get(pk=pk),
                author=author,
                content=content,
            )

        return render(request, 'homepage/create_comment.html', {'post': post})  
    

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'homepage/post_detail.html', context)

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return render(request, 'homepage/post_detail.html', {'post': post})
    return render(request, 'homepage/edit_post.html', {'post': post})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return render(request, 'homepage/post_list.html')
    return render(request, 'homepage/post_delete.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():

            title = request.POST.get('title')
            content = request.POST.get('content')
            status = request.POST.get('status', 'Enabled')  # Default to 'Enabled'
            post = Post.objects.create(title=title, 
                                    content=content, 
                                    status=status, 
                                    author=request.user)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = forms.CreatePost()
    return render(request, 'homepage/post_create.html', {'form': form})  

def create_comment(request, pk):
    if request.method == 'POST':
        author = request.user
        content = request.POST.get('content')
        comment = Post.objects.create(
            post=Post.objects.get(pk=pk),
            author=author,
            content=content,
        )

    return render(request, 'homepage/create_comment.html', {'post': post})  