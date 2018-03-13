from django.views import generic
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


User = get_user_model()

@login_required(login_url = '/login')
def newFriendRequest(request,pk):
    sender=request.user
    receiver=User.objects.get(pk=pk)
    if sender != receiver:
        f=Request(sender=sender,receiver=receiver)
        f.save()
    return redirect('profiles:profileView',receiver)

class FriendRequestView(LoginRequiredMixin, generic.ListView):
    template_name= 'requests/requests.html'
    context_object_name = 'all_requests'

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return user.request_receiver.all()

@login_required(login_url = '/login')
def acceptRequest(request,pk):
    sender=User.objects.get(pk=pk)
    request.user.profile.friends.add(sender)
    sender.profile.friends.add(request.user)
    requests = request.user.request_receiver.all()
    for r in requests:
        if r.sender==sender:
            r.delete()

    return redirect('requests:newFriendRequest',request.user.id)

