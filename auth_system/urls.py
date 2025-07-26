from django.urls import path
from . import views
from .views import follow_user, unfollow_user

urlpatterns = [
   path("login/", views.login_view, name='login'),
   path("logout/", views.logout_view, name='logout'),
   path("profile/", views.user_view, name='profile'),
   path("follow/<int:user_id>/", follow_user, name='follow_user'),
   path("unfollow/<int:user_id>/", unfollow_user, name='unfollow_user'),
]