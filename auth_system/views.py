from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from homepage.models import Post
from . import forms, models
from chat.models import ChatRoom, Message
from auth_system.models import CastomUser, Folow


def login_view(request):
    user_name = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=user_name, password=password)
    if user:
        login(request, user)
        return redirect('post_list')
    return render(request, 'auth_system/login.html')


def logout_view(request):
    logout(request)
    return redirect('post_list')

 
def user_view(request):
    my_post = Post.objects.filter(author=request.user)
    chat_rooms = ChatRoom.objects.filter(author=request.user)
    avatar = 'profile/default_avatar.png'
    context = {
        'my_post': my_post,
        'avatar': avatar,
        'user' : request.user,
        'chat_rooms': chat_rooms,
    }
    return render(request, 'auth_system/profile.html', context)
    
# def register_view(request):

def follow_user(request, user_id):
    following_user = request.user
    Folow.objects.get_or_create(
        follower=CastomUser.objects.get(user=following_user),
        following=CastomUser.objects.get(id=user_id)
    )

def unfollow_user(request, user_id):
    following_user = request.user
    Folow.objects.get_or_create(
        follower=CastomUser.objects.get(user=following_user),
        following=CastomUser.objects.get(id=user_id)
    ).delete()
    #дві проблеми цей шлях і редагування постів
def edit_profile(request):
    cuser = get_object_or_404(CastomUser, user=request.user)
    if request.method == "POST":
        avatar = request.FILES.get("image")
        bio = request.POST.get("bio")
        if bio:   
            cuser.bio = bio
        if avatar:
            cuser.avatar = avatar
        cuser.save()
        return redirect('profile')
    else:
        return render(request, 'auth_system/edit_profile.html', {'cuser':cuser})
    
def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("post_list")
    else:
        form = forms.RegistrationForm()
    return render(request, 'auth_system/register.html', {'form':form})