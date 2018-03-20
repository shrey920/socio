from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

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
        msgs.append(msg)
    context = {}
    context['room'] = room
    context['messages'] = msgs
    context['user'] = request.user
    return render(request, 'chat/chat_index.html', context)

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

@csrf_exempt
def save_message(request):
    # if the request method is a POST request
    if request.method == 'POST':
        # content sent via XMLHttpRequests can be accessed in request.body
        # and it comes in a JSON string, that's why we use json library to
        # turn it into a normal dictionary again
        msg_obj = json.loads(request.body.decode('utf-8'))

        # tries to create the message and save it in the db
        msg = ChatMessage()
        msg.room = ChatRoom.objects.get(pk=msg_obj['room'])
        msg.user = User.objects.get(username=msg_obj['user'])
        msg.text = msg_obj['message']
        msg.save()
                # = ChatMessage.objects.create(user=msg_obj['user_name'], message=msg_obj['message'])
        # if some error occurs it will print the error in the django console and return a HttpResponse
        # containing a error value, which will be received by nodejs socket.io
        # except:
        #     print("error saving message")
        #     return HttpResponse("error")

        # if there aren't any errors, it returns a HttpResponse containing a success value, which will
        # be received by nodejs socket.io
        return HttpResponse("success")

    # if it is a GET request (someone trying to access to the link or something)
    # returns to the main page without doing anything
    else:
        return HttpResponseRedirect('/')
