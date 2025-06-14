from django.urls import path
from . import views

urlpatterns = [
   path("", views.PostListView.as_view(), name='post_list'),
   path("post/<int:pk>/", views.post_detail, name='post_detail'),
   path("post/create/", views.post_create, name='post_create'),
   path("post/delete/<int:pk>/", views.post_delete, name='post_delete'),
   path("post/edit/<int:pk>/", views.edit_post, name='post_edit'),
]