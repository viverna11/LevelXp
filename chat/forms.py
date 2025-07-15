from django import forms
from .models import ChatRoom, Message




class CreateRoomForm(forms.Form):
    room_name = forms.CharField(max_length=100, required=True, label='Room Name')
    description = forms.CharField(widget=forms.Textarea, required=False, label='Description')
    member = forms.CharField(max_length=150, required=False, label='Add Member (Username)')








