from django.urls import path
from . import views

urlpatterns = [
   path("create_room/", views.create_room, name='create_room'),
   path("chat_room/<uuid:room_id>/", views.ChatRoomListView.as_view(), name='chat_room'),
   

]