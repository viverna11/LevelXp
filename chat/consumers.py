import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_room.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_groop_name = f"chat_{self.chat_room.room_name}"
        await self.channel_layer.group_add(
            self.room_groop_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_groop_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']

        await self.save_message(user.username, self.room_name , message)

        await self.channel_layer.group_send(
            self.room_groop_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user.username
            }
        )

    async def message(self, event):
        # Відправляємо повідомлення клієнту
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'user': event['user']
        }))

    @database_sync_to_async
    def save_message(self, username, room_name, message):
        user = User.objects.get(username=username)
        Message.objects.create(
            room_name=room_name,
            user=user,
            message=message
        )
