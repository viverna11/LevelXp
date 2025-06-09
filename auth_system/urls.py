from django.urls import path
from . import views

urlpatterns = [
   path("login/", views.login_view, name='login'),
   path("logout/", views.logout_view, name='logout'),
   path("profile/", views.user_view, name='profile'),
]