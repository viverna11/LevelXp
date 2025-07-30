from django.urls import path
from . import views

urlpatterns = [
   path("", views.PostListView.as_view(), name='post_list'),
   path("post/<int:pk>/", views.post_detail, name='post_detail'),
   path("post/create/", views.post_create, name='post_create'),
   path("post/delete/<int:pk>/", views.post_delete, name='post_delete'),
   path("post/<int:pk>/edit/", views.edit_post, name='post_edit'),
   path("post/<int:pk>/comment_delete/<int:comment_pk>", views.comment_delete, name='comment_delete'),
   
]