from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from homepage.models import Post

def login_view(request):
    user_name = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=user_name, password=password)
    if user:
        login(request, user)
        return render(request, 'homepage/post_list.html')
    return render(request, 'auth_system/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'homepage/post_list.html')


def user_view(request):
    my_post = Post.objects.filter(author=request.user)
    avatar = 'profile/default_avatar.png'
    context = {
        'my_post': my_post,
        'avatar': avatar,
        'user' : request.user,
    }
    return render(request, 'auth_system/profile.html', context)
    
# def register_view(request):