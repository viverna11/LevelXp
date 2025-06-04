from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def login_view(request):
    user_name = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=user_name, password=password)
    if user:
        login(request, user)
        return render(request, 'homepage/home.html')
    return render(request, 'auth_system/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'homepage/home.html')