from django.urls import path
from . import views


urlpatterns = [
   path("login/", views.login_view, name='login'),
   path("logout/", views.logout_view, name='logout'),
   path("profile/", views.user_view, name='profile'),
   path("follow/<int:user_id>/", views.follow_user, name='follow_user'),
   path("unfollow/<int:user_id>/", views.unfollow_user, name='unfollow_user'),
   path("edit_profile/", views.edit_profile, name="edit_profile"),
   path("register", views.register, name='register'),
]