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

User= get_user_model()

class CreateMessageView(LoginRequiredMixin,CreateView):
    login_url = '/login'
    model=Message
    fields = ['message']

    def dispatch(self, request, *args, **kwargs):
        sender = request.user
        receiver = User.objects.get(username=self.kwargs['username'])
        if not receiver in set(sender.profile.friends.all()):
            return redirect('socio:home')
        else:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)

    def form_valid(self, form):
        sender = self.request.user
        receiver = User.objects.get(username=self.kwargs['username'])
        form.instance.sender = sender
        form.instance.receiver = receiver
        if form.is_valid():
            form.save()
            return redirect('socio:home')


class MessagesView(LoginRequiredMixin, generic.ListView):
    template_name='message/messages.html'
    context_object_name = 'all_messages'

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return user.message_receiver.all()