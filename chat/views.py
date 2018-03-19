from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import *

# Create your views here.

User = get_user_model()

class ChatRooms(LoginRequiredMixin, generic.ListView):
    login_url = '/login'
    template_name = 'chat/chat-rooms.html'
    context_object_name = 'all_chats'

    def get_queryset(self):
        user = self.request.user
        return reversed(user.chatroom_set.all())

@login_required(login_url='/login')
def chats(request,pk):
    room = ChatRoom.objects.get(pk=pk)
    cmsgs = ChatMessage.objects.filter(room=room).order_by('-date')[:50]
    msgs = []
    for msg in reversed(cmsgs):
        msgs.append(msg.to_data())
    context = {}
    context['room_id'] = pk
    context['messages'] = msgs
    context['user'] = request.user
    return render(request, 'chat/chats.html', context)

class CreateChatMessageView(LoginRequiredMixin, APIView):
    login_url =  '/login'
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk,  format=None):
        room = ChatRoom.objects.get(pk=pk)
        user = User.objects.get(pk=request.GET['user_id'])
        text = request.GET['text']
        message = ChatMessage()
        message.room = room
        message.user = user
        message.text = text
        message.save()
        context = {
            'room':room.eid,
        }
        return Response(context)