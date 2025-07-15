from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import ChatRoom, Message
from . import forms, models


class ChatRoomListView(ListView):
    model = ChatRoom
    context_object_name = "chat_rooms"
    template_name = 'chat/chat_room_list.html'


def create_room(request):
    if request.method == 'POST':
        form = forms.CreateRoomForm(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            description = form.cleaned_data['description']
            room_id = chat_room.room_id
            chat_room = models.ChatRoom.objects.create(
                room_name=room_name,
                description=description,
                author=request.user
            )
            return redirect('chat_room/', room_id=room_id)
    else:
        form = forms.CreateRoomForm()
    return render(request, 'chat/create_room.html', {'form': form})

def add_member(request, room_id):
    chat_room = models.ChatRoom.objects.get(room_id=chat_room.room_id)
    if request.method == 'Post':
        user = models.User.objects.get(username=request.POST['username'])
        chat_room.member.add(user)
        chat_room.save()
    return redirect('chat_room/', room_id=chat_room.room_id)
